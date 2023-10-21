class DotDict(dict):
    '''General subclass of python dictionary supporting dot-notation to access items.
    The class works case-insensitively, but will retain the case of the key when it was first set.
    The class will'''

    def __call__(self):
        '''Calling of a dictionary subclass should not be possible, instead we raise an error with information about the key and method that were attempted to be called.'''
        head, method = '.'.join(self.get_parent_tree().split('.')[:-1]), self.get_parent_tree().split('.')[-1]
        raise AttributeError(f'Tried to call method "{method}" from {head}, but {head} is empty')

    def __str__(self):
        '''Override str method to prevent printing of hidden keys. You can still print them if you call repr instead of str.'''
        return '{' + ', '.join([f'{key}: {str(val)}' for key, val in self.items()]) + '}'

    def items(self):
        '''We override the items method from dict in order to skip certain keys. We want to hide keys starting and ending
        with dunders, as they should not be exposed to the user.
        '''
        return [(key, self[key]) for key in self.keys()]

    def keys(self):
        original_keys = super().keys()
        return [key for key in original_keys if not (key.startswith('__') and key.endswith('__'))]

    def __getitem__(self, key):
        if key.startswith('__') and key.endswith('__'):
            return None
        self.__set_empty(key)
        val = super().__getitem__(self.__get_case(key))
        return val

    def __getattr__(self, key):
        return self.__getitem__(key)

    def __setitem__(self, key, val):
        # we set the item, but if it is a dict we convert the dict to a DotDict first
        if isinstance(val, dict):
            val = DotDict(val)
        super().__setitem__(self.__get_case(key), val)

    def __setattr__(self, key, val):
        self.__setitem__(key, val)

    def __contains__(self, key):
        # Custom method to check if the key is defined in this object and is also non-empty, case-insensitive.
        return key.lower() in [key_.lower() for key_ in self.keys()] and self[key]

    def __hash__(self):
        '''Hashing of a dictionary subclass should not be possible, instead we should raise an error to let the user know
        that they made a mistake. Also give information of which key was being read.
        '''
        raise KeyError(f'Tried to hash {self.get_parent_tree()}, but it is empty')

    def __bool__(self):
        '''Make sure that keys starting and ending in "__" are skipped'''
        return len([key for key in self.keys() if not (key.startswith('__') and key.endswith('__'))]) > 0

    def get_parent_tree(self):
        '''Method to get the path from this object to the parent object. The result is presented in a formatted string'''
        # every parent except the top-most parent has defined a __parent__ attribute
        if '__parent__' not in self:
            return 'Head'
        # iteratively build the tree using the __name__ attribute.
        parent_names = self.__parent__.get_parent_tree()
        parent_names += '.' + self.__name__
        return parent_names

    def __set_empty(self, key):
        # This function checks if the key has been set. 
        # If it has not, we create a new DotDict object and set it at the desired key
        if self.__get_case(key) not in self.keys():
            val = DotDict()
            # we also keep track of the parent of this object and also the name it was assigned to for later bookkeeping
            val.__parent__ = self
            val.__name__ = key
            self.__setitem__(key, val)

    def __get_case(self, key):
        # Get the case of the key as it has been set in this object.
        # The first time a key-value pair has been assigned the case of the key will be set.
        for key_ in self:
            if key_.lower() == key.lower():
                return key_
        return key

    def prune(self):
        prune(self)


def prune(a: dict) -> None:
    '''Removes values from a dict or DotDict that are set to None.
    
    Args:
        a: Dictionary or dictionary subclass.
    '''
    items = list(a.items())
    for key, value in items:
        try:
            prune(value)
        except AttributeError:
            pass

        if value is None or value == {}:
            del a[key]


def dict_match(a, b):
    matched_keys = [key for key in a.keys() if key in b.keys()]
    match = True
    for key in matched_keys:
        aval, bval = a[key], b[key]
        if isinstance(aval, dict) and isinstance(bval, dict):
            match = dict_match(aval, bval)
        else:
            if aval != bval:
                match = False
    return match


def dict_match_strict(a, b):
    matched_keys = [key for key in a.keys() if key in b.keys()]
    match = True
    for key in matched_keys:
        aval, bval = a[key], b[key]
        if isinstance(aval, dict) and isinstance(bval, dict):
            match = dict_match(aval, bval)
        else:
            if aval != bval:
                match = False
    return match


def dict_to_list(a: dict):
    lst = []
    if not isinstance(a, dict):
        return [[a]]
    for k, v in a.items():
        if isinstance(v, dict):
            if v == {}:
                lst.append([k, {}])
            else:
                [lst.append([k, *x]) for x in dict_to_list(v)]
        else:
            lst.append([k, v])
    return lst


def list_to_dict(a: list):
    d = {}
    for lst in a:
        d_ = d
        for i, key in enumerate(lst):
            if i == len(lst) - 2:
                d_[lst[-2]] = lst[-1]
                break
            else:
                d_ = d_.setdefault(key, {})
    return d


def common_dict(dicts):
    if len(dicts) == 0:
        return {}
    _d = {}
    _d.update(dicts[0])
    for d in dicts:
        for k1, v1 in d.items():
            if k1 not in _d.keys():
                _d[k1] = v1
            elif isinstance(v1, dict):
                _d[k1].update(v1)
    return _d


def union(*dicts):
    sets = [set([tuple(lst) for lst in dict_to_list(dic)]) for dic in dicts]
    ret = set()
    for set_ in sets:
        ret = ret.union(set_)
    return list_to_dict(list(ret))


def intersection(*dicts):
    sets = [set([tuple(lst) for lst in dict_to_list(dic)]) for dic in dicts]
    ret = sets[0]
    for set_ in sets:
        ret = ret.intersection(set_)
    return list_to_dict(list(ret))


def get_inverse(key, dic):
    keys, values = list(dic.keys()), list(dic.values())
    idx = values.index(key)
    return keys[idx]


def invert(dic):
    return {val: key for key, val in dic.items()}


def key_from_value(value, dic):
    for key, val in dic.items():
        if val == value:
            return key


def remove_false_keys(dic):
    to_remove = []
    for key, value in dic.items():
        if not value:
            to_remove.append(key)
    for key in to_remove:
        del(dic[key])
    return dic


def merged_dict(a, b):
    a.update(b)
    return a


def union_non_duplicates(*dicts):
    ''' 
    Merges dicts, but skips keys that occur in multiple dicts but are different

    example:
    a = {"a": 1, "b": 3}
    b = {"a": 2, "b": 3}
    c = {"c": 4}
    union_non_duplicates(a, b, c) == {"b": 3, "c": 4}
    '''
    sets = [set([tuple(lst) for lst in dict_to_list(dic)]) for dic in dicts]
    ret = set()
    for set_ in sets:
        ret = ret.union(set_)
    keys = [ret_[:-1] for ret_ in ret]
    non_duplicates = [key for key in keys if keys.count(key) == 1]
    return list_to_dict([lst for lst in ret if lst[:-1] in non_duplicates])


if __name__ == '__main__':
    d = {'name': 'transitionstate',
         'reactants': {'catalyst': 'catalyst',
                       'radical': 'methyl',
                       'substrate': 'acrolein_E'},
         'reaction': 'Radical Addition',
         'reaction_specific': {},
         'settings_preset': 'BLYP-D3(BJ)/TZ2P/Good',
         'solvent': 'vacuum',
         'substituents': {'catalyst': {'Rcat': 'I2'},
                          'radical': {},
                          'substrate': {'R1': 'pyrrolidine',
                                        'R2': 'm-HOPh',
                                        'R3': 'H',
                                        'R4': 'H',
                                        'Rch': 'O'}}}
    lst = dict_to_list(d)
    print(d)
    print(list_to_dict(lst))

    lst = dict_to_list({'a': [1, 2, 3, 4], 'b': [4, 3, 1]})
    print(lst)

    a = {'test1': 1, 'test2': 2}
    b = {'test1': 1, 'test3': 3}
    c = {'test1': 1, 'test2': 2, 'test3': 3}

    print(union(a, b, c))
    print(intersection(a, b, c))

    a = {"a": 1, "b": 3}
    b = {"a": 2, "b": 3}
    c = {"c": 4}
    print(union_non_duplicates(a, b, c) == {"b": 3, "c": 4})

import dictfunc


def test1():
    lst = [['a', True]]
    a = dictfunc.list_to_dict(lst)
    assert a == {'a': True}


def test2():
    lst = [['a', True], ['b', True]]
    a = dictfunc.list_to_dict(lst)
    assert a == {'a': True, 'b': True}


def test3():
    lst = [['a', True], ['b', 'hello', 'world']]
    a = dictfunc.list_to_dict(lst)
    assert a == {'a': True, 'b': {'hello': 'world'}}


def test4():
    lst = [['a', True], ['b', 'hello', 'world'], ['b', 'hello2', 'world2']]
    a = dictfunc.list_to_dict(lst)
    assert a == {'a': True, 'b': {'hello': 'world', 'hello2': 'world2'}}


if __name__ == '__main__':
    import pytest

    pytest.main()

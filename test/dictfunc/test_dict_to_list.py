import dictfunc


def test1():
    a = {'a': True}
    lst = dictfunc.dict_to_list(a)
    assert lst == [['a', True]]


def test2():
    a = {'a': True, 'b': True}
    lst = dictfunc.dict_to_list(a)
    assert lst == [['a', True], ['b', True]]


def test3():
    a = {'a': True, 'b': {'hello': 'world'}}
    lst = dictfunc.dict_to_list(a)
    assert lst == [['a', True], ['b', 'hello', 'world']]


def test4():
    a = {'a': True, 'b': {'hello': 'world', 'hello2': 'world2'}}
    lst = dictfunc.dict_to_list(a)
    assert lst == [['a', True], ['b', 'hello', 'world'], ['b', 'hello2', 'world2']]


if __name__ == '__main__':
    import pytest

    pytest.main()

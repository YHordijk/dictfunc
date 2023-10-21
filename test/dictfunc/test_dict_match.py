import dictfunc


def test1():
    a = {'a': True}
    b = {'a': True}
    assert dictfunc.dict_match(a, b) is True


def test2():
    a = {'a': True}
    b = {'a': False}
    assert dictfunc.dict_match(a, b) is False


def test3():
    a = {}
    b = {'a': False}
    assert dictfunc.dict_match(a, b) is True


def test4():
    a = {'a': False}
    b = {'a': False, 'b': True}
    assert dictfunc.dict_match(a, b) is True


def test5():
    a = {'a': False}
    b = {'a': False, 'b': True}
    assert dictfunc.dict_match(b, a) is True


def test6():
    a = {'a': True}
    b = {'a': False, 'b': True}
    assert dictfunc.dict_match(a, b) is False


def test7():
    a = {'a': True, 'b': {'c': 'hel', 'd': 'tr'}}
    b = {'a': False, 'b': True}
    assert dictfunc.dict_match(a, b) is False


def test8():
    a = {'a': True, 'b': True}
    b = {'a': False, 'b': True}
    assert dictfunc.dict_match(a, b) is False


def test9():
    a = {'a': True, 'b': True}
    b = {'a': True, 'b': False}
    assert dictfunc.dict_match(a, b) is False


def test10():
    a = {'a': True, 'b': True}
    b = {'a': True, 'b': True}
    assert dictfunc.dict_match(a, b) is True
    

if __name__ == '__main__':
    import pytest

    pytest.main()

import dictfunc


def test1():
    a = dictfunc.DotDict({'a': True})
    b = dictfunc.DotDict({'a': True})
    assert dictfunc.dict_match(a, b) is True


def test2():
    a = dictfunc.DotDict({'a': True})
    b = dictfunc.DotDict({'a': False})
    assert dictfunc.dict_match(a, b) is False


def test3():
    a = dictfunc.DotDict({})
    b = dictfunc.DotDict({'a': False})
    assert dictfunc.dict_match(a, b) is True


def test4():
    a = dictfunc.DotDict({'a': False})
    b = dictfunc.DotDict({'a': False, 'b': True})
    assert dictfunc.dict_match(a, b) is True


def test5():
    a = dictfunc.DotDict({'a': False})
    b = dictfunc.DotDict({'a': False, 'b': True})
    assert dictfunc.dict_match(b, a) is True


def test6():
    a = dictfunc.DotDict({'a': True})
    b = dictfunc.DotDict({'a': False, 'b': True})
    assert dictfunc.dict_match(a, b) is False


def test7():
    a = dictfunc.DotDict({'a': True})
    b = {'a': True}
    assert dictfunc.dict_match(a, b) is True


def test8():
    a = dictfunc.DotDict({'a': True})
    b = {'a': False}
    assert dictfunc.dict_match(a, b) is False


if __name__ == '__main__':
    import pytest

    pytest.main()

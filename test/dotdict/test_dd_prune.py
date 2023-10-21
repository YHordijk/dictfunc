import dictfunc


def test_simple1():
    a = dictfunc.DotDict({'hello': None})
    dictfunc.prune(a)
    assert a == {}


def test_simple2():
    a = dictfunc.DotDict({'hello': False})
    dictfunc.prune(a)
    assert a == {'hello': False}


def test_simple3():
    a = dictfunc.DotDict({'hello': ''})
    dictfunc.prune(a)
    assert a == {'hello': ''}


def test_simple4():
    a = dictfunc.DotDict({'hello': []})
    dictfunc.prune(a)
    assert a == {'hello': []}


def test1():
    a = dictfunc.DotDict({'hello': {'world': None}})
    dictfunc.prune(a)
    assert a == {}


def test2():
    a = dictfunc.DotDict({'hello': {'world': None, 'world2': True}})
    dictfunc.prune(a)
    assert a == dictfunc.DotDict({'hello': {'world2': True}})


def test3():
    a = dictfunc.DotDict({'hello': {'world': None}, 'hello2': {'world': None}})
    dictfunc.prune(a)
    assert a == {}


def test4():
    a = dictfunc.DotDict({'hello': {'world': None}, 'hello2': {'world': None}})
    a.prune()
    assert a == {}


def test5():
    a = dictfunc.DotDict({'hello': {'world': None, 'world2': True}})
    a.prune()
    assert a == {'hello': {'world2': True}}


if __name__ == '__main__':
    import pytest

    pytest.main()

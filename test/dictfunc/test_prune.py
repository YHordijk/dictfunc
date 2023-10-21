import dictfunc


def test_simple1():
    a = {'hello': None}
    dictfunc.prune(a)
    assert a == {}


def test_simple2():
    a = {'hello': False}
    dictfunc.prune(a)
    assert a == {'hello': False}


def test_simple3():
    a = {'hello': ''}
    dictfunc.prune(a)
    assert a == {'hello': ''}


def test_simple4():
    a = {'hello': []}
    dictfunc.prune(a)
    assert a == {'hello': []}


def test1():
    a = {'hello': {'world': None}}
    dictfunc.prune(a)
    assert a == {}


def test2():
    a = {'hello': {'world': None, 'world2': True}}
    dictfunc.prune(a)
    assert a == {'hello': {'world2': True}}


def test3():
    a = {'hello': {'world': None}, 'hello2': {'world': None}}
    dictfunc.prune(a)
    assert a == {}


if __name__ == '__main__':
    import pytest

    pytest.main()

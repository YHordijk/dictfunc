import dictfunc


def test1():
    a = {"a": 1, "b": 3}
    b = {"a": 2, "b": 3}
    assert dictfunc.intersection(a, b) == {"b": 3}


def test2():
    a = {"a": 1}
    b = {"a": 2}
    assert dictfunc.intersection(a, b) == {}


def test3():
    a = {"a": 1}
    assert dictfunc.intersection(a) == a


def test4():
    a = {}
    assert dictfunc.intersection(a) == {}


def test5():
    a = {}
    b = {'a': 10}
    assert dictfunc.intersection(a, b) == {}


def test6():
    a = {'a': {'b': 'world'}}
    b = {'a': {'b': 'world', 'b2': 'world2'}}
    assert dictfunc.intersection(a, b) == {'a': {'b': 'world'}}


def test7():
    a = {"a": 1, "b": 3}
    b = {"a": 2, "b": 3}
    c = {"c": 4, 'b': 3}
    assert dictfunc.intersection(a, b, c) == {"b": 3}


if __name__ == '__main__':
    import pytest 

    pytest.main()

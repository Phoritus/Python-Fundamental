import pytest

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a/b

def test_mul():
    assert multiply(10,5) == 50
    assert multiply(20,2) == 40
    assert multiply(17,9) == 153

def test_divide():
    assert divide(10,0) == 5

    with pytest.raises(ValueError):
        divide(10,0)
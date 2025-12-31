def add(a,b):
    return a+b

def test_add():
    assert add(2,5) == 7
    assert add(-1,-5) == -6

def test_add_big_number():
    assert add(200000,3000000) == 3200000
    assert add(-100000,5000000) == 4900000
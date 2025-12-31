import pytest
from inventory_management import Inventory

@pytest.fixture
def pd():
    pd = Inventory()
    yield pd

def test_add_stock(pd):
    pd.add_stock('Gummy',50)
    item = pd.stock
    assert item is not None
    assert item['Gummy'] == 50

def test_remove_stock(pd):
    pd.add_stock('Pepo',200)
    pd.remove_stock('Pepo',59)
    pd.remove_stock('Pepo',42)
    item = pd.stock
    assert item['Pepo'] == 99
    with pytest.raises(ValueError):
        assert pd.remove_stock('Pepo',5000)

def test_check_availability(pd):
    pd.add_stock('Pepo', 856)
    pd.remove_stock('Pepo', 145)
    assert pd.check_availability('Pepo',382) is True
    assert pd.check_availability('Pepo',9999) is False

def test_remove_stock_with_insufficient_inventory(pd):
    pd.add_stock('Milk',30)
    with pytest.raises(ValueError):
        assert pd.remove_stock('Milk',40)

def test_full_inventory_cycle(pd):
    pd.add_stock('Pepo',503)
    pd.remove_stock('Pepo',392)
    assert pd.check_availability('Pepo',110) is True
    pd.remove_stock('Pepo',10)
    assert pd.check_availability('Pepo',500) is False


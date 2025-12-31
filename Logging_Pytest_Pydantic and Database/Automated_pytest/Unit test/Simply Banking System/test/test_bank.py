import pytest

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print('Project root:',project_root)
sys.path.insert(0, project_root)

from src.banking import BankingSystem

def test_create_account():
    account = BankingSystem('King',500)
    assert account.owner == 'King'
    assert account.balance == 500

def test_deposit():
    account = BankingSystem('King')
    account.deposit(50)
    account.deposit(60)
    assert account.balance == 110
    with pytest.raises(ValueError):
        assert account.deposit(-10)

def test_withdraw():
    account = BankingSystem("Kdend",385)
    account.withdraw(60)
    account.withdraw(97)
    assert account.balance == 228
    with pytest.raises(ValueError):
        assert account.withdraw(500)

@pytest.mark.skip(reason='The reason xyz is')
def test_getbalance():
    account = BankingSystem("Kdend", 385)
    assert account.balance == 385



from typing import List, Dict, Optional, Any
from datetime import date
import json
import os
from logging_setup import setup_logging

# Setup logger
logger = setup_logging('db_helper')

# File path for storing expenses
DATA_FILE = 'expenses.json'

def load_data() -> List[Dict]:
    """
    Load expenses data from JSON file
    Returns:
        List of expenses
    """
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return []
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return []

def save_data(data: List[Dict]) -> bool:
    """
    Save expenses data to JSON file
    Args:
        data: List of expenses to save
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        return True
    except Exception as e:
        logger.error(f"Error saving data: {e}")
        return False

def get_all_data() -> List[Dict]:
    """
    Fetch all expenses
    Returns:
        List of all expenses
    """
    logger.info('Fetching all expenses')
    return load_data()

def get_by_date(expense_date: date) -> List[Dict]:
    """
    Fetch expenses for a specific date
    Args:
        expense_date: Date to fetch expenses for
    Returns:
        List of expenses for the specified date
    """
    logger.info(f'Fetching expenses for date: {expense_date}')
    expenses = load_data()
    return [exp for exp in expenses if exp['expense_date'] == str(expense_date)]

def insert_data(expense_date: date, amount: float, category: str, notes: str) -> bool:
    """
    Insert a new expense record
    Args:
        expense_date: Date of the expense
        amount: Amount of the expense
        category: Category of the expense
        notes: Additional notes
    Returns:
        bool: True if successful, False otherwise
    """
    logger.info(f'Inserting expense for date {expense_date}')
    try:
        expenses = load_data()
        new_expense = {
            'id': len(expenses) + 1,
            'expense_date': str(expense_date),
            'amount': amount,
            'category': category,
            'notes': notes
        }
        expenses.append(new_expense)
        return save_data(expenses)
    except Exception as e:
        logger.error(f"Error inserting expense: {e}")
        return False

def delete_data(expense_date: date) -> bool:
    """
    Delete expenses for a specific date
    Args:
        expense_date: Date to delete expenses for
    Returns:
        bool: True if successful, False otherwise
    """
    logger.info(f'Deleting expenses for date {expense_date}')
    try:
        expenses = load_data()
        expenses = [exp for exp in expenses if exp['expense_date'] != str(expense_date)]
        return save_data(expenses)
    except Exception as e:
        logger.error(f"Error deleting expenses: {e}")
        return False

def get_by_id(expense_id: int) -> Optional[Dict]:
    """
    Fetch expense by ID
    Args:
        expense_id: ID of the expense to fetch
    Returns:
        Expense record if found, None otherwise
    """
    logger.info(f'Fetching expense with ID: {expense_id}')
    expenses = load_data()
    for expense in expenses:
        if expense['id'] == expense_id:
            return expense
    return None

def fetch_sum_date(start_date: date, end_date: date) -> List[Dict]:
    """
    Fetch expense summary by category for a date range
    Args:
        start_date: Start date of the range
        end_date: End date of the range
    Returns:
        List of category-wise expense summaries
    """
    logger.info(f'Fetching expense summary from {start_date} to {end_date}')
    try:
        expenses = load_data()
        filtered_expenses = [
            exp for exp in expenses 
            if start_date <= date.fromisoformat(exp['expense_date']) <= end_date
        ]
        
        # Calculate totals by category
        category_totals = {}
        for expense in filtered_expenses:
            category = expense['category']
            amount = expense['amount']
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
        
        # Convert to list of dictionaries
        return [
            {'category': cat, 'Total': total}
            for cat, total in category_totals.items()
        ]
    except Exception as e:
        logger.error(f"Error fetching expense summary: {e}")
        return []

def fetch_sum_months() -> List[Dict]:
    """
    Fetch monthly expense summary for the current year
    Returns:
        List of monthly expense summaries
    """
    logger.info('Fetching monthly expense summary')
    try:
        expenses = load_data()
        current_year = date.today().year
        
        # Filter expenses for current year
        yearly_expenses = [
            exp for exp in expenses 
            if date.fromisoformat(exp['expense_date']).year == current_year
        ]
        
        # Calculate monthly totals
        monthly_totals = {}
        for expense in yearly_expenses:
            month = date.fromisoformat(expense['expense_date']).month
            amount = expense['amount']
            if month in monthly_totals:
                monthly_totals[month] += amount
            else:
                monthly_totals[month] = amount
        
        # Convert to list of dictionaries
        return [
            {'month': month, 'total': total}
            for month, total in sorted(monthly_totals.items())
        ]
    except Exception as e:
        logger.error(f"Error fetching monthly summary: {e}")
        return []






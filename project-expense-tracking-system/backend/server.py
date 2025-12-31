import streamlit as st
from datetime import date
import pandas as pd
from typing import List, Dict

# Initialize session state for storing expenses if it doesn't exist
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Function to get expenses by date
def get_by_date(expense_date: date) -> List[Dict]:
    """
    Get expenses for a specific date
    Args:
        expense_date: The date to filter expenses
    Returns:
        List of expenses for the specified date
    """
    return [exp for exp in st.session_state.expenses if exp['date'] == expense_date]

# Function to add or update expenses
def add_or_update(expense_date: date, expenses_data: List[Dict]):
    """
    Add or update expenses for a specific date
    Args:
        expense_date: The date for the expenses
        expenses_data: List of expense items to add/update
    """
    # Remove existing expenses for this date
    st.session_state.expenses = [exp for exp in st.session_state.expenses if exp['date'] != expense_date]
    
    # Add new expenses
    for expense in expenses_data:
        st.session_state.expenses.append({
            'date': expense_date,
            'amount': expense['amount'],
            'category': expense['category'],
            'notes': expense['notes']
        })

# Function to get expenses summary by date range
def fetch_sum_date(start_date: date, end_date: date) -> Dict:
    """
    Get expense summary by category for a date range
    Args:
        start_date: Start date of the range
        end_date: End date of the range
    Returns:
        Dictionary with category-wise expense summary
    """
    filtered_expenses = [exp for exp in st.session_state.expenses 
                        if start_date <= exp['date'] <= end_date]
    
    if not filtered_expenses:
        return {}
    
    # Calculate totals by category
    df = pd.DataFrame(filtered_expenses)
    category_totals = df.groupby('category')['amount'].sum()
    total_amount = category_totals.sum()
    
    # Calculate percentages
    result = {}
    for category, amount in category_totals.items():
        result[category] = {
            'Total': float(amount),
            'Percentage': float((amount / total_amount) * 100)
        }
    
    return result

# Function to get monthly expense summary
def fetch_sum_months() -> Dict:
    """
    Get monthly expense summary
    Returns:
        Dictionary with monthly expense totals
    """
    if not st.session_state.expenses:
        return {}
    
    df = pd.DataFrame(st.session_state.expenses)
    df['month'] = pd.to_datetime(df['date']).dt.month
    monthly_totals = df.groupby('month')['amount'].sum()
    
    month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    
    return {month_names[month]: {'Total': float(total)} 
            for month, total in monthly_totals.items()}

# Streamlit UI
st.title('Expense Tracking System')

# Sidebar for navigation
page = st.sidebar.selectbox(
    "Choose a page",
    ["Add Expenses", "View Expenses", "Analytics"]
)

if page == "Add Expenses":
    st.header("Add New Expenses")
    
    # Date input
    expense_date = st.date_input("Select Date", date.today())
    
    # Dynamic expense inputs
    num_expenses = st.number_input("Number of expenses to add", min_value=1, value=1)
    
    expenses_data = []
    for i in range(num_expenses):
        st.subheader(f"Expense {i+1}")
        amount = st.number_input(f"Amount {i+1}", min_value=0.0, value=0.0)
        category = st.text_input(f"Category {i+1}")
        notes = st.text_input(f"Notes {i+1}")
        
        if amount and category:  # Only add if required fields are filled
            expenses_data.append({
                'amount': amount,
                'category': category,
                'notes': notes
            })
    
    if st.button("Save Expenses"):
        add_or_update(expense_date, expenses_data)
        st.success("Expenses saved successfully!")

elif page == "View Expenses":
    st.header("View Expenses")
    
    # Date filter
    selected_date = st.date_input("Select Date to View", date.today())
    
    expenses = get_by_date(selected_date)
    if expenses:
        df = pd.DataFrame(expenses)
        st.dataframe(df)
    else:
        st.info("No expenses found for this date")

else:  # Analytics page
    st.header("Expense Analytics")
    
    # Date range selector
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", date.today().replace(day=1))
    with col2:
        end_date = st.date_input("End Date", date.today())
    
    # Show category-wise summary
    st.subheader("Category-wise Summary")
    summary = fetch_sum_date(start_date, end_date)
    if summary:
        df_summary = pd.DataFrame.from_dict(summary, orient='index')
        st.dataframe(df_summary)
        
        # Show pie chart
        st.subheader("Expense Distribution")
        chart_data = pd.DataFrame({
            'Category': list(summary.keys()),
            'Amount': [data['Total'] for data in summary.values()]
        })
        st.bar_chart(chart_data.set_index('Category'))
    else:
        st.info("No expenses found for the selected date range")
    
    # Show monthly summary
    st.subheader("Monthly Summary")
    monthly_summary = fetch_sum_months()
    if monthly_summary:
        df_monthly = pd.DataFrame.from_dict(monthly_summary, orient='index')
        st.dataframe(df_monthly)
        
        # Show bar chart
        st.subheader("Monthly Expense Trend")
        chart_data = pd.DataFrame({
            'Month': list(monthly_summary.keys()),
            'Amount': [data['Total'] for data in monthly_summary.values()]
        })
        st.bar_chart(chart_data.set_index('Month'))
    else:
        st.info("No monthly data available")
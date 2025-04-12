transactions = []

type = input('Income or Expense?').lower()
category = input('Category?').lower()
amount = float(input('Amount?'))



#Function to append transaction array
def add_transactions(type, amount, category):
    transactions = {
        'type': type,
        'amount': amount,
        'category': category
    }
    transactions.append(transactions)
print('Transaction added successfully!')

#Summary Function 
def view_summary():
    income = sum(t['amount'] for t in transactions if t ['type'] == 'income')
    expenses = sum(t['amount'] for t in transactions if t ['type'] == 'expense')
    balance = income - expenses

    print('Summary:')
    print(f'Total Income: {income}')
    print(f'Total Expenses: {expenses}')
    print(f'Balance: {balance}')

def save_to_cvs(filename = 'budget_log.csv'):
    



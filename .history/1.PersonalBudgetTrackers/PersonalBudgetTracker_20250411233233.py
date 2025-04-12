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
    with open (filename, 'w') as file: 
        file.write('Type,Category,Amount\n')
        for t in transactions:
            line = file.write(f"{t['type']},{t['category']},{t['amount']}\n")
            file.write(line)
    print('Transactions saved to budget_log.csv')

def load_from_csv(filename = 'budget_log.csv'):
    import os
    if not os.path.exists(filename):
        print('File not found!')
        return
    
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            type, category, amount = line.strip().split(',')
            transactions.append({
                'type': type,
                'category': category,
                'amount': float(amount)
            })
    print('Transactions loaded from budget_log.csv')



transactions = []

# Function to append transaction to the list
def add_transaction(trans_type, amount, category):
    transaction = {
        'type': trans_type,
        'amount': amount,
        'category': category
    }
    transactions.append(transaction)
    print('Transaction added successfully!')

# Summary Function 
def view_summary():
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = income - expenses

    print('\nSummary:')
    print(f'Total Income: {income}')
    print(f'Total Expenses: {expenses}')
    print(f'Balance: {balance}')

# Save to CSV
def save_to_csv(filename='budget_log.csv'):
    with open(filename, 'w') as file:
        file.write('Type,Category,Amount\n')
        for t in transactions:
            file.write(f"{t['type']},{t['category']},{t['amount']}\n")
    print('Transactions saved to budget_log.csv')

# Load from CSV
def load_from_csv(filename='budget_log.csv'):
    import os
    if not os.path.exists(filename):
        print('No existing file found.')
        return

    with open(filename, 'r') as file:
        next(file)  # skip header
        for line in file:
            trans_type, category, amount = line.strip().split(',')
            transactions.append({
                'type': trans_type,
                'category': category,
                'amount': float(amount)
            })
    print('Transactions loaded from budget_log.csv')

# Menu system
def menu():
    load_from_csv()

    while True:
        print('\n--- Budget Tracker Menu ---')
        print('1. Add Transaction')
        print('2. View Summary')
        print('3. Save and Exit')

        choice = input('Choose an option: ')

        if choice == '1':
            trans_type = input('Income or Expense? ').lower()
            category = input('Category? ').lower()
            try:
                amount = float(input('Amount? '))
                add_transaction(trans_type, amount, category)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            view_summary()
        elif choice == '3':
            save_to_csv()
            print('Goodbye!')
            break
        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    menu()

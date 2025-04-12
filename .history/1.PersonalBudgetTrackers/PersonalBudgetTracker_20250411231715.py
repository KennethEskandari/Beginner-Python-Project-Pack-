transactions = []

type = input('Income or Expense?')
amount = input('Enter the amount:')
category = input('Enter the category:')


#Function to append transaction array
def add_transactions(type, amount, category):
    transactions = {
        'type': type,
        'amount': amount,
        'category': category
    }
    transactions.append(transactions)
    print('Transactions Added!')


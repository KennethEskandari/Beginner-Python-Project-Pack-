transactions = []

type = input('Income or Expense?').lower()
category = input('Category?').lower()
amount = flooat(input('Amount?'))



#Function to append transaction array
def add_transactions(type, amount, category):
    transactions = {
        'type': type,
        'amount': amount,
        'category': category
    }
    transactions.append(transactions)
    print('Transactions Added!')


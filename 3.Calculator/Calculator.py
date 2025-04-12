# Defining Functions 
def add(x,y):
    return x + y 

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y 

def divide(x, y):
    if y == 0: 
        raise ValueError("Cannot Divide By Zero")
    return x / y 

#User Interface 
def user_input():
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Choose 1 - 4 :")

    return choice 

#The Calculator a
def calculator():
    while True:
        choice = user_input()

        if choice not in['1','2','3','4']:
            print("Invalid Choice")
            continue

        try:
            num1 = (float(input('Enter First Number: ')))
            num2 = (float(input('Enter Second Number:')))
        
            if choice == '1': 
                result = add(num1,num2)
            elif choice == '2':
                result = subtract(num1,num2)
            elif choice == '3':
                result = multiply(num1,num2)
            elif choice == '4':
                result = divide(num1,num2)

            print(f'Result: {result}')
        except ValueError as e: 
            print(f'Error: {e}')
        except Exception as e:
            print(f'Error: {e}')

        again = input("Another Calculation?")
        if again.lower() != 'y':
            break

if __name__ == '__main__':
    calculator()
# Defining Functions 
def add(x,y):
    return x + y 

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y 

def divide(x, y):
    if y == 0: 
        raise KeyError("Cannot Divide By Zero")
    return x / y 

#User Interface 
def user_interface():
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Choose 1 - 4 :")

    return choice 
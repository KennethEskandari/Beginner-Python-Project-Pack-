import random

secret_number = random.int(1, 100)

guess = None 
print("I am thinking of a number between 1 and 100. Can you guess what it is?")

while guess != secret_number:
    try: 
        guess = int(input("Enter Your Number : "))
    except ValueError as e:
        print(f'Error: : {e}')

        
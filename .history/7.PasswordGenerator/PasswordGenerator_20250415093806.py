import random
import string 

length = int(input("Enter The Length Of Desired Password: "))
include_numbers = input('Include Numbers? : (yes/no)').lower() == 'yes'
include_symbols = input('Include Symbols? : (yes/no)').lower() == 'yes'

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation    

char_pool = letters 

if include_numbers:
    char_pool += numbers
if include_symbols:
    char_pool += symbols

password = ''.join(random.choice(char_pool) for _ in range(length))
print(f'Your Password Is : {password}')





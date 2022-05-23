print('Welcome to password generator app')

import random


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

symbol = ['!', '#', '$', '£', '@', '%', '&', '(', ')', '*', '+']


num_letter = int(input('How many letters would you like in your password?\n'))
num_symbol = int(input(f"How many symbols would you like?\n"))
numbers = int(input(f"How many numbers would you like?\n"))


password = []

for char in range(1, num_letter + 1):
    password.append(random.choice(letters))

for char in range(1, num_symbol + 1):
    password.append(random.choice(symbol))

for char in range(1, numbers + 1):
    password.append(random.choice(number))

random.shuffle(password)

if len(password) < 6:
    print('Password length must not be less than 6. Please try again.')
else:
    new_password = ''.join([str(pword) for pword in password])

    print(f'Your password is {new_password}')
    

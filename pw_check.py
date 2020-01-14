username = input("What is your username? ")
password = input('What is your password? ')
length = len(password)
hidden_password = '*' * length
print(f'{username}, your password {hidden_password} is {length} letters long')


password = 'Password'
print("Enter login:")
login_input = input()
print('Enter password')
while (pass_input := input()) != password:
    print(f'Password for user: {login_input} is incorrect')
    print('Please try again...')
else:
    print(f'Password for user: {login_input} is correct')



def welcome_user():
    print("Welcome to the Brain Games!")
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')

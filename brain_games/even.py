from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')


def random_number():
    return randint(1, 100)


def answer_yes_no():

    answer = ''
    while answer == '':
        print('Your answer: ', end='')
        answer = input()
    return answer


def right_answer(guess):
    if int(guess) % 2 == 0:
        return 'yes'
    else:
        return 'no'


def access():
    x = 1
    while x <= 3:
        riddle = random_number()
        print(f'Question: {riddle}')
        answer = answer_yes_no()
        if right_answer(riddle) == answer:
            print('Correct!')
            x += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{right_answer(riddle)}'.
Let's try again, {name}!""")
            return access()
    print(f"Congratulations, {name}!")

def even_start():
    print('brain-even\n')
    welcome_user()
    instruction = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(f'{instruction}')
    access()

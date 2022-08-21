import random


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}!')


def answer_yes_no():
    answer = ''
    while answer == '':
        print('Your answer: ', end='')
        answer = input()
    return answer


def right_answer(riddle, x, y):
    if riddle == 'add':
        return str(x + y)
    elif riddle == 'mul':
        return str(x * y)
    elif riddle == 'sub':
        return str(x - y)
    else:
        print('unexpected value')


def random_quiz():
    return random.choice(['add', 'mul', 'sub'])


def access():
    for i in range(3):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        riddle = random_quiz()
        if riddle == 'add':
            print(f'Question: {x} + {y}')
        elif riddle == 'mul':
            print(f'Question: {x} * {y}')
        elif riddle == 'sub':
            print(f'Question: {x} - {y}')
        else:
            print('unexpected value')
        answer = answer_yes_no()
        if right_answer(riddle, x, y) == answer:
            print('Correct!')
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{right_answer(riddle, x, y)}'.
Let's try again, {name}!""")
            return access()
    print(f"Congratulations, {name}!")


def start():
    print('brain-calc\n')
    welcome_user()
    instruction = 'What is the result of the expression?'
    print(f'{instruction}')
    access()

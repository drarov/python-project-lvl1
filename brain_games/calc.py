import random
import prompt
import sys


def welcome_user():
    print("Welcome to the Brain Games!")
    return prompt.string('May I have your name? ')


def answer_yes_no():
    return prompt.string('Your answer: ')


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


def access(name):
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
            return sys.exit
    print(f"Congratulations, {name}!")


def start():
    print('brain-calc\n')
    name = welcome_user()
    print(f'Hello, {name}!')
    instruction = 'What is the result of the expression?'
    print(f'{instruction}')
    access(name)

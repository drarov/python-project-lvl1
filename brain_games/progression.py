import random
import prompt
import sys


def welcome_user():
    print("Welcome to the Brain Games!")
    return prompt.string('May I have your name? ')


def answer_yes_no():
    return prompt.string('Your answer: ')


def access(name):
    for i in range(3):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        list1 = []
        for n in range(x, x + y * 10, y):
            list1.append(n)
        z = random.randint(0, len(list1) - 1)
        right_answer = str(list1[z])
        list1.pop(z)
        list1.insert(z, '..')
        quiz = ''
        for el in list1:
            quiz += str(f'{el} ')
        print(f"Question: {quiz}")
        answer = answer_yes_no()
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.\n"
                  f" Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return sys.exit
        print(f"Congratulations, {name}!")


def start():
    print('brain-progression\n')
    name = welcome_user()
    print(f'Hello, {name}!')
    instruction = 'What number is missing in the progression?'
    print(f'{instruction}')
    access(name)

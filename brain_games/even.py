from random import randint
import prompt
import sys


def welcome_user():
    print("Welcome to the Brain Games!")
    return prompt.string('May I have your name? ')


def random_number():
    return randint(1, 100)


def answer_yes_no():
    return prompt.string('Your answer: ')


def right_answer(guess):
    if int(guess) % 2 == 0:
        return 'yes'
    else:
        return 'no'


def access(name):
    for i in range(3):
        riddle = random_number()
        print(f'Question: {riddle}')
        answer = answer_yes_no()
        if right_answer(riddle) == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.\n"
                  f" Correct answer was '{right_answer(riddle)}'.")
            print(f"Let's try again, {name}!")
            return sys.exit
    print(f"Congratulations, {name}!")


def even_start():
    print('brain-even\n')
    name = welcome_user()
    print(f'Hello, {name}!')
    instruction = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(f'{instruction}')
    access(name)

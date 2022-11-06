import random
import prompt
from primePy import primes
import sys


def welcome_user():
    print("Welcome to the Brain Games!")
    return prompt.string('May I have your name? ')


def answer_yes_no():
    return prompt.string('Your answer: ')


def right_answer(quiz):
    if primes.check(quiz) is True and quiz > 1:
        return 'yes'
    else:
        return 'no'


def access(name):
    for i in range(3):
        quiz = random.randint(1, 10)
        print(f"Question: {quiz}")
        answer = answer_yes_no()
        if right_answer(quiz) == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.\n"
                  f" Correct answer was '{right_answer(quiz)}'.")
            print(f"Let's try again, {name}!")
            return sys.exit
    print(f"Congratulations, {name}!")


def start():
    print('brain-prime\n')
    name = welcome_user()
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    access(name)

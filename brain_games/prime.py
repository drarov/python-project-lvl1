import random
import prompt
from primePy import primes


def welcome_user():
    print("Welcome to the Brain Games!")
    return prompt.string('May I have your name? ')


def answer_yes_no():
    return prompt.string('Your answer: ')


def right_answer(quiz):
    if primes.check(quiz):
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
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{right_answer(quiz)}'.
Let's try again, {name}!""")
            return access(name)
    print(f"Congratulations, {name}!")


def start():
    print('brain-prime\n')
    name = welcome_user()
    print(f'Hello, {name}!')
    instruction = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    print(f'{instruction}')
    access(name)

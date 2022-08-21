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


def comparison1(num1):
    list1 = []
    for i in range(num1, 0, -1):
        list1.append(i)
        div_list1 = []
        for n in list1:
            if num1 % n == 0:
                div_list1.append(n)
    return div_list1


def comparison2(num2):
    list2 = []
    for i in range(num2, 0, -1):
        list2.append(i)
        div_list2 = []
        for n in list2:
            if num2 % n == 0:
                div_list2.append(n)
    return div_list2

def right_answer(num1, num2):
    list1 = comparison1(num1)
    list2 = comparison2(num2)
    com_list = []
    for i in list1:
        for n in list2:
            if i == n:
                com_list.append(i)
    return str(max(com_list))


def access():
    for i in range(3):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print(f'Question: {x}, {y}')
        answer = answer_yes_no()
        if right_answer(x, y) == answer:
            print('Correct!')
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{right_answer(x, y)}'.
Let's try again, {name}!""")
            return access()
    print(f"Congratulations, {name}!")


def start():
    print('brain-gcd\n')
    welcome_user()
    instruction = 'Find the greatest common divisor of given numbers.'
    print(f'{instruction}')
    access()


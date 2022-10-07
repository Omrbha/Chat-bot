def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('\nPlease, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('\nLet me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('\nNow I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("\nLet's test your programming knowledge.\n")
    # write your code here
    print("Why do we use functions?\n")
    print("1. To make our code complex.\n2. To make a comment in our code.\n3. To make our code reusable.\n4. To stop the code from running.")
    result = ""
    while result != "Right":
        answer = input()
        if answer == "3" :
            result = "Right"
        else:
            print("Please, try again")
    print('Completed, have a nice day!\n')
    print("Why do we use methods?\n")
    print("1. To repeat a statement multiple times.\n2. To decompose a program into several small subroutines.\n3. To determine the execution time of a program.\n4. To interrupt the execution of a program.")
    result = ""
    while result != "Right":
        answer = input()
        if answer == "2" :
            result = "Right"
        else:
            print("Please, try again")
    print('Completed, have a nice day!\n')


def end():
    print('Congratulations, have a nice day!\n')


greet('Brat', '2022')  # change it as you need
remind_name()
guess_age()
count()
# ...
test()
end()

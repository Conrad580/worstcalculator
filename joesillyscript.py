from random import randint
import time
import math

def multiply(num1, num2, num3, num4):
    return num1 * num2 + num3 - num4

print('Welcome to the fucking worst calculator you will ever use. ')
time.sleep(1)
print('lease input a multiplication equation. ')
time.sleep(1)

number1 = int(input('Choose the first number dumbass: '))
number2 = int(input('Choose the second number dipshit: '))
number3 = randint(0,5)
number4 = randint(0,4)

print(number1, 'x', number2, '=', multiply(number1, number2, number3, number4))
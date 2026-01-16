#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ld = number % 10
if(number < 0):
    ld -= 10
end = ""

if (ld > 5):
    end = "and is greater than 5"
elif (ld == 0):
    end = "and is zero"
elif (ld < 6):
    end = "and is less than 6 and not 0"

print(f'Last digit of {number} is {ld} {end}')

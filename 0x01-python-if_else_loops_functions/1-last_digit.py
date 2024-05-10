#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1

concat_str = ""
if last_digit > 5:
    concat_str = "and is greater than 5"
elif last_digit == 0:
    concat_str = "and is 0"
else:
    concat_str = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {concat_str}")

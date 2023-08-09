
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    digit = number % 10
else:
    digit = number % (-10)
    
if digit > 5:
    print("Last last digit of {} is {} and is greater than 5".format(number, digit))
elif digit == 0:
        print("Last last digit of {} is {} and is greater than 0".format(number, digit))
else:
    print("Last last digit of {} is {} and is less than 6 and not 0".format(number, digit))

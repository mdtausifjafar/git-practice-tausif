# Importing the datetime module to work with dates
import datetime

print("My name is: Md. Tausif Jafar")
print("Today's date:", datetime.datetime.now().strftime("%d-%m-%Y"))


# Importing the 'add', 'subtract', 'multiply', and 'divide' functions from the utils.py file
from utils import add, subtract, multiply, divide

print("Addition of 5 and 3:", add(5, 3))
print("Subtraction of 5 from 3:", subtract(5, 3))
print("Multiplication of 5 by 3:", multiply(5, 3))
print("Division of 5 by 3:", divide(5, 3))
print("Division of 5 by 0:", divide(5, 0))
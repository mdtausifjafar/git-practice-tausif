import datetime

print("My name is: Md. Tausif Jafar")

print("Today's date:", datetime.datetime.now().strftime("%d-%m-%Y"))


# Call the functions from utils.py

from utils import add, subtract

print("Addition of 5 and 3:", add(5, 3))

print("Subtraction of 5 and 3:", subtract(5, 3))
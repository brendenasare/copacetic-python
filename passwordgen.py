import random
from random import choice
import string

name = input("What is your name: ").capitalize()
age = input("How old are you: ")
colour = input("What is your favourite colour: ").capitalize()
special = "!,@,#,$,%"
lengthOfPassword = 12

pass_char = list(name + age + colour + special)


def password_generator():

	#shuffling  characters
	random.shuffle(pass_char)
	
	#picking random characters from the list
	password = []
	for i in range(lengthOfPassword):
		password.append(random.choice(pass_char))

	#shuffling the resultant password
	random.shuffle(password)

	#converting the list to string
	#printing the list
	print("".join(password))

# invoking the function to print password  times
for i in range(6):
	password_generator()


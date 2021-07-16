import string
from random import randrange as random

possibleCharacters = string.ascii_lowercase

print("Would you like your password to include uppercase letters? (Type y for yes and n for no)")
uppercase = input()

if uppercase == "y":
  possibleCharacters += string.ascii_uppercase

print("Would you like your password to include numbers?")
numbers = input()

if numbers == "y":
  possibleCharacters += string.digits

print("Would you like your password to include punctuation?")
punctuation = input()

if punctuation == "y":
  possibleCharacters += string.punctuation

password = ""

print("How many characters would you like your password to be?")
length = int(input())

for x in range(length):
  password += possibleCharacters[random(len(possibleCharacters))]

print(f"Your password is: {password}")

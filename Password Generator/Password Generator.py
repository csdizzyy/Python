from random import randrange
from string import ascii_letters, digits, punctuation


character_list = ascii_letters + digits + punctuation

def generate_password(length, amount):
    for i in range(amount):
        password = ""
        for i in range(length):
            password += character_list[randrange(len(character_list))]
        print(password)

amount = int(input("Passwords to be generated: "))
length = int(input("Password Length: "))
(generate_password(length, amount))
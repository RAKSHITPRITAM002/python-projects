import random
char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()-_+={}[]|\\;:"<>,./?'
length=int(input("Enter password length:"))
password=""

for a in range(length):
    password=random.choice(char)
    print(password)
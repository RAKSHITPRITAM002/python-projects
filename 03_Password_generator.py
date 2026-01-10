import random
char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()-_+={}[]|\\;:"<>,./?'
length=int(input("Enter password length:"))
password = ''.join(random.choice(char) for i in range(length))
print("Generate password:", password)

    
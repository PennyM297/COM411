print("What is your name human?")
name = input()

print("How old are you? (In years)")
age = int(input())

print("How tall are you? (In meters)?")
height = float(input())

print("How much do you weigh? (In kilograms)")
weight = int(input())
total = float(weight/(height*height))

print(f"{name} you are {age} years old and your bmi is {total}")




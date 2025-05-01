# Heather Rossio
# 02/10/2025
# P1HW2
# Python Second homework

print("This program calculates and displays travel expenses")
user_budg = int(input("Enter your budget: "))
print()
user_dest = input("Enter your travel destination: ")
print()
user_gas = int(input("Enter how much you will spend on gas: "))
print()
user_accom = int(input("Enter how much you will spend on accomidations:"))
print()
user_food = int(input("Enter how much you will spend on food:"))


print("---------Travel Espenses----------")


print("Location:", user_dest)
print("Initial Budget:", user_budg)
print()

print("Fuel:", user_gas)
print("Accomodation:", user_accom)
print("Food:", user_food)
print()

ex_budg = user_food + user_gas + user_accom
new_budg = user_budg - ex_budg

print("Remaining Balance:", (new_budg))



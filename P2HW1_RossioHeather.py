# Heather Rossio
# 02/26/2025
# P2HW1
# Python  homework formatting strings

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


print(f"{'Location:':<25} {user_dest}")
print(f"{'Initial Budget:' :<25} ${user_budg :.2f}")

print()

print(f"{'Fuel:':<25} ${user_gas :.2f}")
print(f"{'Accomodation:':<25} ${user_accom :.2f}")
print(f"{'Food:':<25} ${user_food :.2f}")
print()

ex_budg = user_food + user_gas + user_accom
new_budg = user_budg - ex_budg

print(f"{'Remaining Balance:' :<25} ${new_budg :.2f}")


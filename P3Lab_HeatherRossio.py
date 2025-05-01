# Heather Rossio
# 03/03/25
# P3LAB
# Use if/else statements to determine coin combination

# Get float from user and convert to integer. 
input_money = float(input("Enter the amount of money as a float: $"))

money = int(input_money * 100)

# print(money)

# Calculate number of whole dollars

num_dollars = money // 100
# print(f"Num dollars: {num_dollars}")

# Remove thedollars from the amount of money

money = money - (num_dollars * 100)
# print(f"The remaining money is: {money}")



# Calculate number of quarters

num_quarters = money // 25
# 2.65
# print(f"Num quarters: {num_quarters}")

# Remove the quarters from the amount of money

money = money - (num_quarters * 25)
# print(f"The remaining money is: {money}")



# Calculate number of dimes

num_dimes = money // 10
# print(f"num dimes: {num_dimes}")

# Remove the dimesfrom the amount of money

money = money - (num_dimes * 10)
# print(f"The remaining money is: {money}")


# Calculate number of nickles

num_nickels = money // 5
# print(f"num nickles: {num_nickels}")

# Remove the dimesfrom the amount of money

money = money - (num_nickels * 5)
# print(f"The remaining money is: {money}")

num_pennies = money

# Display coins/dolars needed only if they are used
# Ensure all grammer is correct 
print()
print()
print()

print(f"{input_money:.2f}")
#If no change is due display "No Change"
if input_money  <= 0.00:
    print("No Change")

if num_dollars > 0:
    if num_dollars ==1:
        print(f"{num_dollars} Quarter")
    else:
        print(f"{num_dollars} Quarters")

if num_quarters > 0:
    if num_quarters ==1:
        print(f"{num_quarters} Quarters")
    else:
        print(f"{num_quarters} Quarters")
        
if num_dimes > 0:
    if num_dimes ==1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

if num_nickels > 0:
    if num_nickels ==1:
        print(f"{num_nickels} Nickel")
    else:
        print(f"{num_nickels} Nickels")

if num_pennies > 0:
    if num_pennies ==1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")
               
               
        


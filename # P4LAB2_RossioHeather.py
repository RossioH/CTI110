# P4LAB2
# 03/19/25
# Heather Rossio
# Loop multiplication program


# create variable to create out while loop 

run_again = "yes"

while run_again != "no":
    # Get int from user
    user_num = int(input("Enter an integer:"))
    if user_num < 0: 
        print("negative numbers are not allowed")

    else: # user num is 0 or greater
        for i in range(1,13):
         print(f"{user_num} * {i} = {user_num *i}")

    run_again = input("Would you like to run again? 'yes'/'no': ")

# while loop ends here
print("Program has ended")
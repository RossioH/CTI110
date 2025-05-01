# Heather Rossio
# P2HW2
# 02/24/2025
# Lists

# get 6 grades from user. They should be floats.   
module1 = float(input( 'Enter grade for module 1: '))
module2 = float(input(' Enter grade for module 2: '))
module3 = float(input( 'Enter grade for module 3: '))
module4 = float(input( 'Enter grade for module 4: '))
module5 = float(input( 'Enter grade for module 5: '))
module6 = float(input( 'Enter grade for module 6: '))

# Create an empty list
grades_list = []

# Use append method to add al greades into the list
# code looks like this:  list_name.append(what_to_add_to_list)

grades_list.append(module1)
grades_list.append(module2)
grades_list.append(module3)
grades_list.append(module4)
grades_list.append(module5)
grades_list.append(module6)

# Display list
print(grades_list)
print()

# Display Valuesfor user
print('------------Results---------')
print(f"{'Lowest Grade:' :<20} {min(grades_list)}")
print(f"{'Hghest Grade:' :<20} {max(grades_list)}")
print(f"{'Sum of Grades:':<20} {sum(grades_list)}")

average = sum(grades_list)/len(grades_list)
print(f"{'Average:' :<20} {average:.2f}")
print('-----------------------------------------------')

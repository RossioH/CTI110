# P3HW1
# Rossio Heather
# 03/15/25
# Debug and fix program


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades_list = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades_list)
high = max(grades_list)
sum_total = sum(grades_list)
print('------------Results------------')
print(f"{'Lowest Grade:' :<20} {min(grades_list)}")
print(f"{'Hghest Grade:' :<20} {max(grades_list)}")
print(f"{'Sum of Grades:':<20} {sum(grades_list)}")
average = sum(grades_list)/len(grades_list)
print(f"{'Average:' :<20} {average:.2f}")

# determine letter grade for average
print("-----------------------------------------")

if average >= 90:
 print('Your grade is: A')
elif average >= 80:
 print('Your grade is: B')
elif average >= 70:
 print('Your grade is: C')
elif average >= 60:
 print('Your grade is: D')
else:
 print('Your grade is: F') 
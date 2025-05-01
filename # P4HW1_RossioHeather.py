# P4HW1
# Heather Rossio
# 03/28/25
# upgrade grade program to loop 


#Create variable num_scores (int) -> user input number of scores
num_scores = int(input('How many scores would you like to enter?: '))
# Create an empty list -> scores_list
scores_list = []
# for each in range (num_scores)
for each in range(num_scores):
    score = int(input(f"Enter score # {each+1}: "))
 #while score is < 0 or score is >100
    while score < 0 or score > 100:
        # print('INVALID. Score must be betwen 0 and 100') 
        print('INVALID. Score must be betwen 0 and 100') 
        score = int(input(f"Enter score # {each+1} again: "))
    
    scores_list.append(score)
print(scores_list) 

#Get the lowest score in list -> assign it to a variable
#Remove the lowest score from the list
lowest_score = min(scores_list)
scores_list.remove(lowest_score)
print('---------------Results---------------')
print()
print(f"{'Lowest Grade:' :<20} {(lowest_score)}")
print(f"{'Modified list:' :<20} {(scores_list)}")

#Get average of list after removing lowest score
average_grade = sum(scores_list)/len(scores_list)
print(f"{'Average:' :<20} {average_grade:.2f}")
#Use average to determine letter grade
if average_grade >= 90:
    print(f"{'Grade:' :.20} {'A'} ")
elif average_grade >= 80:
    print(f"{'Grade:' :.20} {'B'} ")
elif average_grade >= 70:
    print(f"{'Grade:' :.20} {'C'} ")
elif average_grade >= 60:
    print(f"{'Grade:' :.20} {'D'} ")
elif average_grade <=59:
    print(f"{'Grade:' :.20} {'F'} ")





 


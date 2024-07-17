#Dalyn Stiles
#July 4th 2024 (happy fourth of July!)
#P4HW2

#Asks user for the number of scores
num_scores=int(input(f'How many scores do you want to enter?'))

#Create a list to store the scores
scores = []

i = 0
while i < num_scores:
    score = float(input(f'Enter Score #{i+1}:'))
    while score < 0 or score > 100:
        print(f'INVALID Score Entered! ! ! !')                                      #Create a loop
        print(f'Score must be between 0 and 100')
        score = float(input(f'Enter score #:{i+1}'))
    scores.append(score)
    i+=1

print('-----------------------RESULTS----------------------')
lowest_score = min(scores)
print(f'Lowest score :  {lowest_score}')

modified_scores = scores.copy()
modified_scores.remove(lowest_score)
print(f'Modified list :  {modified_scores}')

average_score = sum(modified_scores) / len(modified_scores)
print(f'Scores average : {average_score:.2f}' )

if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
elif average_score >= 0:
    letter_grade = 'F'
else:
    print(f'Retake this class.')

print(f'Grade : {letter_grade}')
print('--------------------------------------------')
import random


def scores_and_grades():
    for i in range(0, 9):
        temp_random = int((random.random() * (100 - 60 + 1)) + 60)
        if temp_random >=60 and temp_random <= 69:
            print "Score: " + str(temp_random) + "; Your grade is D"
        elif temp_random >=70 and temp_random <= 79:
            print "Score: " + str(temp_random) + "; Your grade is C"
        elif temp_random >=80 and temp_random <= 89:
            print "Score: " + str(temp_random) + "; Your grade is B"
        elif temp_random >=90 and temp_random <= 99:
            print "Score: " + str(temp_random) + "; Your grade is A"


scores_and_grades()
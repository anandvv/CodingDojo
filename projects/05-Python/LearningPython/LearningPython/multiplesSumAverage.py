
#Assignment: Multiples, Sum, Average

#Multiples - Part 1
#Write code that prints all the odd numbers from 1 to 1000. 
i=1
while i < 1000:
    if (i % 2) > 0:
        print i
    i += 1

#Multiples - Part 2
#Create another program that prints all the multiples of 5 from 5 to 1,000,000
#j=5
while j < 1000001:
    if (j % 5) == 0:
        print j
    j += 1

#Sum List
#print the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
sum = 0;

for everyNumber in a:
    sum += everyNumber

print "Sum:", sum

#Average List
#print the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
print "Average:", sum/len(a)
'''
.find()
.replace()
min()
max()
.sort()
.len()
'''

#Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
firstInstanceOfWord = words.find("day")
print firstInstanceOfWord

newWords = words.replace("day", "month")
print newWords

#Min and Max
x = [2,54,-2,7,12,98]
print "Min: ", min(x)
print "Max", max(x)

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print "First:", x[0]
print "Last:", x[len(x)-1]

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x

y = []

for i in range(0, 5):
    y.append(x[i])

print y

z = []
for i in range(5, 11):
    z.append(x[i])

print z

k = []
k.append(y)
print k

for i in z:
    k.append(i)

print k




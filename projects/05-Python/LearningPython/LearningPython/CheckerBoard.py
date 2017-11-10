list1 = ['*', ' ', '*', ' ', '*', ' ', '*', ' ']
list2 = [' ', '*', ' ', '*', ' ', '*', ' ', '*']

string1 = ""
string2 = ""

for i in range(0, 4):
    for item in list1:
        string1 += item
    for item in list2:
        string2 += item

    print string1
    print string2

    string1 = ""
    string2 = ""




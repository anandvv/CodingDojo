def TypeList(x):
    new_string = ""
    numSum = 0
    for value in x:
        if isinstance(value,int) or isinstance(value,float):
            numSum += value
        elif isinstance(value,str):
            new_string += value  

    if new_string and numSum:
        print "String:", new_string
        print "Sum:", numSum
        print "This list is of mixed type"
    elif new_string:
        print "String:", new_string
        print "This list is of string type"
    else:
        print "Sum:", numSum
        print "This list is of integer type"

#input
l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

TypeList(l1)
TypeList(l2)
TypeList(l3)

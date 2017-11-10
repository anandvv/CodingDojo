def compareLists(l1, l2):
    isIdentical = False

    if len(l1) == len(l2):
        #do something
        for i in range(0, len(l1)):
            if type(l1[i]) == type(l2[i]):
                if l1[i] == l2[i]:
                    isIdentical = True
                else:
                    isIdentical = False

        if isIdentical:
            print "The two lists are identical"
        else:
            print "The two lists are not identical"
    else:
        print "The two lists are not identical"

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compareLists(list_one, list_two)

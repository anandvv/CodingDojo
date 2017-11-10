# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number.


def odd_even():
    for i in range(1, 2001):
        if i % 2 == 0:
            print "Number is " + str(i) + "." + " This is an even number."
        else:
            print "Number is " + str(i) + "." + " This is an odd number."


# Multiply using a new list
def multiply(a, number):
    b = []
    for item in a:
        b.append(item * number)
    return b


# Multiply and update the same list items
def multiply1(a, number):
    i = 0
    for item in a:
        a[i] = (item * number)
        i += 1
    return a


def layered_multiples(arr):
    new_array = []
    temp_array = []
    for item in arr:
        for i in range(0, item):
            temp_array.append(1)
        new_array.append(temp_array)
        temp_array = []
    return new_array


# Test the functions

# odd_even()

inputList = [2, 4, 5]
print inputList

outputList = multiply1(inputList, 3)
print outputList

x = layered_multiples(multiply1([2, 4, 5], 3))
print x

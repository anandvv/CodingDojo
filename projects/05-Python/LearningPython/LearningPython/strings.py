name = "Zen"
y = 42

print "My name is", name, y

#the following won't work with concatenation
name = "Karma"
print "My name is" + name

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

#Strings - Built in methods
x = "Hello World"
print x.upper()

#prints the number of substrings
x = "able was i ere i saw elba"
y = "i"
print "Number of occurences of i:", x.count(y)

#returns a boolean
print "End with elba:", x.endswith("elba")

#retuns the staring index of the first occurence of a substring
print "Starting Index of substring 'ere':", x.find("ere")

#returns true if the string is alphanumeric, alphabets, digit etc
print "Is AlphaNumeric: ", x.isalnum()
print "Is Alphabets:", x.isalpha()
print "Is Digit",  x.isdigit()

#join 
l = ["anand", "vidyullata", "vijay"]
print "Joined:", "$".join(l)

#split
toSplit = "anand$vidyullata$vijay"
print "Splitting ", toSplit, ":", toSplit.split("$")




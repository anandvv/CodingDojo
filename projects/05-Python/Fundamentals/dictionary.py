myDict = {"name": "Anand", "age": "41", "countryOfBirth": "India", "favoriteLanguage": "Python"}


def print_dictionary(x):
    print "My name is " + x["name"]
    print "My age is " + x["age"]
    print "I was born in " + x["countryOfBirth"]
    print "My favorite language is " + x["favoriteLanguage"]

    for item in x.keys():
        print x[item]

    for item in x.values():
        print item

print_dictionary(myDict)


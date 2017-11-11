users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def names(x):
    studentDictionary = x["Students"]
    # print studentDictionary
    instructorDictionary = x["Instructors"]
    # print instructorDictionary

    i = 1
    print "Students"
    for item in studentDictionary:
        print str(i) + " - " + item["first_name"].upper() + " " + item["last_name"].upper() + " - " \
              + str(len(item["first_name"]) + len(item["last_name"]))
        i += 1

    i = 1
    print "Instructors"
    for item in instructorDictionary:
        print str(i) + " - " + item["first_name"].upper() + " " + item["last_name"].upper() + " - " \
              + str(len(item["first_name"]) + len(item["last_name"]))
        i += 1



names(users)

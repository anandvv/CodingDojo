var students = [ 
    {first_name:  'Michael', last_name : 'Jordan'},
    {first_name : 'John', last_name : 'Rosales'},
    {first_name : 'Mark', last_name : 'Guillen'},
    {first_name : 'KB', last_name : 'Tonel'}
]

// for(var student in students){
//     console.log(students[student].first_name + " " + students[student].last_name);
// }

var users = {
    'Students': [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
     ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
     ]
};

var students = users["Students"];
for(var student in students){
    console.log((parseInt(student) + 1) + " - " + students[student].first_name + " " + students[student].last_name + " - " + (parseInt(students[student].first_name.length) + parseInt(students[student].last_name.length)));
}
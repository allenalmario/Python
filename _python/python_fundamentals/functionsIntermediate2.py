# 1

# 1
x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)
# 2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = "Bryant"
print(students)

# 3

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

# 4

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30

print(z)

# 2

def iterateDictionary(some_list):
    for item in some_list:
        for k,v in item.items():
            print(k + " - " + v)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students)

# 3

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        count = 0
        for items in some_dict[key]:
            count += 1
        print(str(count) + " " + key.upper())
        for items in some_dict[key]:
            print(items)

printInfo(dojo)
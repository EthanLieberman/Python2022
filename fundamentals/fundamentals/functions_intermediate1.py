# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15

# students[0]['first_name'] = 'Bryant'
# sports_directory['soccer'][0] = 'Andres'
# z[0]['y'] = 30

# print(x)
# print(students)
# print(sports_directory)
# print(z)





students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterateDictionary(stu):
    # for i in len(stu):
    #     print(stu[i])
    for key in stu:
        print(key)


iterateDictionary(students)




# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]


# def iterateDictionary2(key,list):
#     for i in list:
#         print(i[key])


# iterateDictionary2('first_name', students)




# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }


# # dictionary[key_name][index#]

# # def printInfo(el):
# #     print(len(el['basketball']))
# #     for i in el['basketball']:
# #         print(i)
# #     print()
# #     print(len(el['soccer']))
# #     for i in el['soccer']:
#         # print(i)


# def printInfo(el):
#     for key in el:
#         print(len(el[key]))
#         for name in el[key]:
#             print(name)
#         print()





# printInfo(sports_directory)

# friends = [
#     {
#         "name": "Dodo",
#         "age": "24",
#         "power": "shittalk",
#         "fav_nums": [1, 4, 6, 3],
#     },
#     {
#         "name": "Beni",
#         "age": "24",
#         "power": "volume",
#         "fav_nums": [1, 4, 6, 3],
#     },
#     {
#         "name": "Bó",
#         "age": "23",
#         "power": "sass",
#         "fav_nums": [1, 4, 6, 3],
#     }
# ]

# print(friends[2]['name'])
# print(friends[2]['fav_nums'][2])

# # return shortStrList[[x in longStr for x in shortStrList].index(True)]

# def name_finder(friends, name):
#     # if any(friend['name'] == name for friend in friends):
#     #     index = friends.index()
#     print([friend["name"] == name for friend in friends])
#     return friends[[friend["name"] == name for friend in friends].index(True)]


# res = name_finder(friends, 'Bó')
# print(res)


arr = list(range(10, 20))

for ind, num in enumerate(arr):
    print(ind, " : ", num)

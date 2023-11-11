# 1
# user_1 = []
# user_2 = []
# user_3 = []
#
# consumer_info = [user_1, user_2, user_3]
#
# names = []
# surnames = []
# ages = []
#
# full_data = [names, surnames, ages]
#
# for i in range(0, 3):
#     name = input("შეიყვანეთ სახელი: ")
#     names.append(name)
#     surname = input("შეიყვანეთ გვარი: ")
#     surnames.append(surname)
#     age = input("შეიყვანეთ ასაკი: ")
#     ages.append(age)
#
# k = 0
# while k < len(consumer_info):
#     for user in consumer_info:
#         user.append(full_data[k][consumer_info.index(user)])
#     k += 1
#
# while True:
#     disp_inp = int(input("შეიყვანეთ ინდექსი 0/2: "))
#     if disp_inp in range(0, 3):
#         print("""
#   Name:{0}
#   Lastname:{1}
#   Age:{2}
#                  """.format(consumer_info[disp_inp][0],
#                             consumer_info[disp_inp][1], consumer_info[disp_inp][2]))
#         break
#     else:
#         print("შეიყვანეთ სწორი ინდექსი!")




# 2

# print("დარეგისტრირდით ჩვენს საიტზე.")
# user_data = []
# log_in = False
# while True:
#     name = input("შეიყვანეთ სახელი: ")
#     if name == "":
#         print("სახელი არ უნდა იყოს ცარიელი!")
#     else:
#         if log_in:
#             break
#         while True:
#             password = input("შეიყვანეთ პაროლი: ")
#             if len(password) < 8:
#                 print("შეიყვანეთ სწორი პაროლი!")
#             else:
#                 user_data.append(name)
#                 user_data.append(password)
#                 print("ცადეთ შემოსვლა ჩვენს საიტზე.")
#                 while True:
#                     log_in_name = input("შეიყვანეთ სახელ ი: ")
#                     if log_in_name != user_data[0]:
#                         print("შეიყვანეთ სწორი სახელი!")
#                     else:
#                         if log_in:
#                             break
#                         while True:
#                             log_in_password = input("შეიყვანეთ პაროლი: ")
#                             if log_in_password != user_data[1]:
#                                 print("შეიყვანეთ სწორი პაროლი!")
#                             else:
#                                 print("თქვენ შემოსული ხართ ჩვენს საიტზე.")
#                                 log_in = True
#                                 if log_in:
#                                     break



# 3

# actors = [
#           ['John', 'Depp', 'USA', '60', '1.78'],
#           ['Antonio', 'Banderas', 'Spain', '63', '1.74'],
#           ['Brad', 'Pitt', 'USA', '59', '1.8'],
#           ['Gerard', 'Depardieu', 'France', '74', '1.8'],
#           ['Leonardo', 'Dicaprio', 'USA', '48', '1.83'],
#           ['Mario', 'Cimaro', 'Cuba', '52', '1.88'],
#           ['Adriano', 'Celentano', 'Italy', '85', '1.78']
# ]
#
# name_or_surname = input("enter  name or surname of the actor: ").capitalize()
#
# for actor in actors:
#     if name_or_surname in actor:
#         print("""
#         name:{0}
#         surname:{1}
#         country:{2}
#         age:{3}
#         height:{4}
#         """.format(actor[0], actor[1], actor[2], actor[3], actor[4]))


#X&O

# my_map = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# x_results = []
# o_results = []
#
# x_wins = False
# o_wins = False
#
# win_combs = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
#              [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
#
# c = [5, 2, 9, 3, 1]
#

# while True:
#     player_1 = int(input("enter number 1/9: "))
#     for row in my_map:
#         for index, item in enumerate(row):
#             if player_1 == item:
#                 x_results.append(item)
#                 row.pop(index)
#                 row.insert(index, "X")
#                 break
#     for comb in win_combs:
#         k = 0
#         for num in comb:
#             if num in x_results:
#                 k += 1
#         if k == 3:
#             x_wins = True
#
#     print(my_map[0])
#     print(my_map[1])
#     print(my_map[2])
#     if x_wins:
#         print("x wins")
#         break
#
#     player_2 = int(input("enter number 1/9: "))
#     for row in my_map:
#         for index, item in enumerate(row):
#             if player_2 == item:
#                 o_results.append(item)
#                 row.pop(index)
#                 row.insert(index, "O")
#                 break
#     for comb in win_combs:
#         k = 0
#         for num in comb:
#             if num in o_results:
#                 k += 1
#         if k == 3:
#             o_wins = True
#
#     print(my_map[0])
#     print(my_map[1])
#     print(my_map[2])
#     if o_wins:
#         print("o wins")
#         break
#
#     if len(x_results) >= 5 or len(o_results) >= 5:
#         if o_wins == False and x_wins == False:
#             print('draw')
#             break

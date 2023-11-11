# ჩაძირობანა
#
# from random import choice
#
# comp_positions = []
# user_positions = []
#
# for num in range(1, 21):
#     comp_positions.append(num)
#     user_positions.append(num)
#
# def sinking(pos1=4, pos2=5, pos3=7, pos4=18, pos5=14, pos6=17):
#
#     user_active = 6
#     comp_active = 6
#     rand_pos = []
#     rand_indt_list = comp_positions[:]
#
#     for num in range(0, 6):
#         rand = choice(rand_indt_list)
#         rand_pos.append(rand)
#         rand_indt_list.remove(rand)
#
#     comp_ships = [['comp1', [rand_pos[0]]], ['comp2', [rand_pos[1], rand_pos[2]]],
#                   ['comp3', [rand_pos[3], rand_pos[4], rand_pos[5]]]]
#
#     user_ships = [['user1', [pos1]], ['user2', [pos2, pos3]],
#                   ['user3', [pos4, pos5, pos6]]]
#
#     while True:
#         user_attack = int(input('attack the position of computer\'s ships: '))
#         if user_attack in user_positions:
#             user_positions.remove(user_attack)
#             for ship in comp_ships:
#                 if user_attack in ship[1]:
#                     ship[1].remove(user_attack)
#                     comp_active -= 1
#                     print(f'{ship[0]} lost {user_attack}-th position!')
#                     print(f'Computer left {comp_active} positions')
#                 if len(ship[1]) == 0:
#                     comp_ships.remove(ship)
#                     print(f'{ship[0]} is sunk!')
#             if comp_active < 1:
#                 print("You won!")
#                 break
#         else:
#             print("Enter only unused numbers between 1 and 20!")
#
#         comp_attack = choice(comp_positions)
#         if comp_attack in comp_positions:
#             comp_positions.remove(comp_attack)
#             for ship in user_ships:
#                 if comp_attack in ship[1]:
#                     ship[1].remove(comp_attack)
#                     user_active -= 1
#                     print(f'{ship[0]} lost {comp_attack}-th position!')
#                     print(f'You left {user_active} positions')
#
#                 if len(ship[1]) == 0:
#                     user_ships.remove(ship)
#                     print(f'{ship[0]} is sunk!')
#
#             if user_active < 1:
#                 print("Computer won!")
#                 break
#
# user_pos=[4,7,19,5,18,16]
# sinking(*user_pos)

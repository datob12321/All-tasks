#1

# import random
# choice_list = ["scissors", "rock", "paper"]
# computer_points=human_points=0
#
# while True:
#     computer_choice = random.choice((choice_list))
#     human_choice = input("Enter one of the following: scissors/rock/paper: ").lower()
#     print(f"Computer choose {computer_choice}")
#     if human_choice in choice_list:
#         if human_choice==computer_choice:
#             print("Nothing")
#         elif (human_choice=="scissors" and computer_choice=="paper") or (human_choice=="paper"
#         and computer_choice=="rock") or (human_choice=="rock" and computer_choice=="scissors"):
#             human_points+=1
#             if human_points!=3:
#                 print(f"You have {human_points} points.")
#             else:
#                 print("You won!")
#         else:
#             computer_points+=1
#             if computer_points!=3:
#                 print(f"Computer has {computer_points} points.")
#             else:
#                 print("Computer won!")
#     else:
#         print("Invalid input!")
#     if human_points==3 or computer_points==3:
#         break





#2

# input_range=int(input("Enter the number: "))
# for i in range(1,input_range+1):
#     for j in range(1,input_range+1):
#         print(i*j, end=" ")
#     print()






#3

# budget=3000
#
# while True:
#     expense=int(input("Enter the expense: "))
#     if budget>=expense:
#         if expense!=0:
#             budget-=expense
#         else:
#             print(f"You have left {budget} ₾ on the account.")
#             break
#     else:
#         print("You have not enough money on the account!")






#4

# while True:
#     user_input=input("Enter the text: ")
#     if user_input.lower()!="quit":
#         print(f"User Said Whaaat!?\nUser Said {user_input}")
#     else:
#         break
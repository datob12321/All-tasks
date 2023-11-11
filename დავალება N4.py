#1

# user_inp = input("Enter some text: ")
# digits = letters = others = 0
#
# for i in user_inp:
#     if i.isdigit():
#         digits += 1
#     elif i.isalpha():
#         letters += 1
#     else:
#         others += 1
#
# print("We have {2} digits, {0} letters and {1} other characters."
#       .format(letters, others, digits))





#2

# inp_1 = input("Enter a text: ")
# inp_2 = input("Enter some text again: ")
#
# first_char = inp_1[0]
# second_char = inp_2[-1]
# third_char = inp_1[1]
# fourth_char = inp_2[-2]
#
# our_string = "{0}{1}{2}{3}".format(first_char, second_char, third_char, fourth_char)
#
# print(our_string)



#3

# inp_1 = input("Enter a text: ")
# inp_2 = input("Enter some text again: ")
#
# inp1_not_in_inp2 = inp2_not_in_inp1 = 0
#
# for char in inp_2:
#     if char not in inp_1:
#         inp2_not_in_inp1 += 1
#
# for char in inp_1:
#     if char not in inp_2:
#         inp1_not_in_inp2 += 1
#
# if inp1_not_in_inp2 == 0 and inp2_not_in_inp1 == 0:
#     print("Strings are balanced!")
# else:
#     print("Strings are not balanced!")

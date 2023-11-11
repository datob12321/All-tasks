# 1 შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას,
# თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).


# def unique_list(par_list):
#     to_set = set(par_list)
#     to_list = list(to_set)
#     return to_list
#
# list1 = [1, 4, 2, 5, 4, 6, 4, 5, 3, 4, 1, 'dato', 3, 10,21, 'bitsadze', 'dato']
# print(unique_list(list1))






# 2 შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს
# უნიკალური ელემენტებით, რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).


# def immutable_set(par_list1):
#     to_set_1 = set(par_list1)
#     return frozenset(to_set_1)
#
# mylist = [4, 5, 1, 2, 'dato', 7, 'dato', True, -12, 2]
# immutable = immutable_set(mylist)
# print(immutable)






# 3 შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ,
# შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.


# def set_to_tuple(par_set_1, par_set_2):
#     if type(par_set_1) == set and type(par_set_2) == set:
#         united = par_set_1.union(par_set_2)
#         to_tuple = tuple(united)
#         return to_tuple
#     else:
#         print("Both parameters must be set!")
#
# set1 = {1, 42, 6, 'Donald Trump', 15, 10, True}
# set2 = {120, 3, 15, ('x*2=25', '-5,5'), 'Aleko Elisashvili', 11, False, True, 30}
# print(set_to_tuple(set1, set2))






# 4 შექმენი ფუნქცია რომელიც მიიღებს მომხმარებლის სახელს და პაროლს, ასევე სიის სახელს.
# პაროლს გაუკეთებს ჰეშირებას და მონაცემს შეინახავს tuple ტიპის
# მონაცემად გადაცემულ სიაში. შედეგი უნდა დააბრუნოს [("user1", "pass1")]

# name = input('Enter your name: ')
# password = input('Enter your password: ')

#
# def user_info(outer_list, name, password):
#     import bcrypt
#     salt = bcrypt.gensalt()
#     encoded = password.encode()
#     hashed_password = bcrypt.hashpw(encoded, salt)
#     to_tuple = (name, hashed_password)
#     outer_list.append(to_tuple)
#     return outer_list
#
# my_list = []
# print(user_info(my_list, name, password))

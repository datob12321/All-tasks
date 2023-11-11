#1
# def multiplication(arr,b):
#     mult = lambda a: a * b
#     multiplied = map(mult, arr)
#     return list(multiplied)
#
# s = [1, 5, 4, 6, 5, -3, -4, 10]
# print(multiplication(s,3))





#2
# def upper_list_size(list1):
#     upper = lambda a: a.isupper()
#     filtered = filter(upper, list1)
#     return len(list(filtered))
#
# names = ['DATO', 'GivI', 'Gio', 'NINI']
# print(upper_list_size(names))






#3
# def two_sum(arr):
#     from functools import reduce
#     mylambda = lambda a: a if a > 0 else None
#     mylambda1 = lambda a: a if a < 0 else None
#     pos = filter(mylambda, arr)
#     neg = filter(mylambda1, arr)
#     reduce_pos_sum = reduce(lambda a, b: a+b, pos)
#     reduce_neg_sum = reduce(lambda a, b: a+b, neg)
#     return reduce_neg_sum, reduce_pos_sum
#
# nums = [5, 8, -6, 15, -12, -21, 7, 3]
# print(two_sum(nums))







#4

# def bank(budget):
#     while True:
#         try:
#             expense = int(input("Enter the expense: "))
#             if budget >= expense:
#                 if expense != 0:
#                     budget -= expense
#                 else:
#                     print(f"You have left {budget} ₾ on the account.")
#                     break
#             else:
#                 print("You have not enough money on the account!")
#         except:
#             print("Enter only hole numbers, not letters, float numbers or other symbols!")
#
# bank(5000)
# 1
# from random import randint
#
# num_arr = []
#
# for i in range(0, 10):
#     num_arr.append(randint(0, 100))
#
# num_arr.sort()
#
# print(num_arr)






# 2
# from random import randint
#
# num_arr = []
#
# for num in range(0, 10):
#     num_arr.append(randint(100, 1000))
#
# sorted_reversed = sorted(num_arr, reverse=True)
#
# print(sorted_reversed)







# 3
# def time_counting(func):
#     from time import time
#     def wrapper(arr):
#         start_time = time()
#         result = func(arr)
#         end_time = time()
#         print(end_time-start_time)
#         return result
#     return wrapper
#
# def ran_num_arr(min = 0, max = 100, length = 10):
#     from random import randint
#     arr = []
#     for num in range(0, length):
#         arr.append(randint(min, max))
#     return arr
#
# @time_counting
# def selection_sort(array):
#     for i in range(0, len(array)-1):
#         for j in range(i+1, len(array)):
#             if array[i] > array[j]:
#                 array[i], array[j] = array[j], array[i]
#     return array
#
# @time_counting
# def bubble_sort(array):
#     length = len(array)-1
#     sorteD = False
#     while not sorteD:
#         sorteD = True
#         for i in range(0, length):
#             if array[i] > array[i+1]:
#                 sorteD = False
#                 array[i], array[i+1] = array[i+1], array[i]
#     return array
#
# bubble_sort(ran_num_arr(0, 200, 1000))
# selection_sort(ran_num_arr(0, 200, 1000))
# print()
# bubble_sort(ran_num_arr(0, 200, 2000))
# selection_sort(ran_num_arr(0, 200, 2000))
# print()
# bubble_sort(ran_num_arr(0, 200, 3000))
# selection_sort(ran_num_arr(0, 200, 3000))

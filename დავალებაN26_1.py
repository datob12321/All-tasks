import threading
import time
import concurrent.futures as features


def find_odds(num_list: list[int]):
    for num in num_list:
        if num % 2 == 0:
            print(num, end=' ')
    print()


def find_evens(num_list: list[int]):
    for num in num_list:
        if num % 2 == 1:
            print(num, end=' ')


my_arr = list(range(30, 51))

start = time.time()

# 1
# thread_odds = threading.Thread(target=find_odds, args=(my_arr,))
# thread_evens = threading.Thread(target=find_evens, args=(my_arr,))
# thread_odds.start()
# thread_evens.start()
# thread_odds.join()
# thread_evens.join()


# 2
with features.ThreadPoolExecutor() as executor:

    thread_odd = executor.submit(find_odds, my_arr)
    thread_even = executor.submit(find_evens, my_arr)


end = time.time()

print(f'\ntime - {end - start}')

import random
import time

def brick_sort(unordered_list: list[int]) -> list[int]:
    while True:

        is_sorted = True
        for i in range(0, len(unordered_list)-1, 2):
            if unordered_list[i] > unordered_list[i+1]:
                unordered_list[i], unordered_list[i+1] = unordered_list[i+1], unordered_list[i]
                is_sorted = False
            else:
                unordered_list[i], unordered_list[i+1] = unordered_list[i], unordered_list[i+1]

        for i in range(1, len(unordered_list)-1, 2):
            if unordered_list[i] > unordered_list[i+1]:
                unordered_list[i], unordered_list[i+1] = unordered_list[i+1], unordered_list[i]
                is_sorted = False
            else:
                unordered_list[i], unordered_list[i+1] = unordered_list[i], unordered_list[i+1]

        if is_sorted == True:
            break
    return unordered_list

list_length = 10000
unordered_list = random.sample(range(1, 2*list_length), list_length)

start = time.time()
ordered_list = brick_sort(unordered_list)
end = time.time()

print(ordered_list)
print(end-start)

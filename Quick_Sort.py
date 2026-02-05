import random
import time

def quicksort(list):
    if len(list) <= 1:
        return list 
    
    pivot = list[0]     #alternative list[random.randint(0, len(list)-1)]
    smaller_nums, bigger_nums, pivot_nums = [], [], []

    for i in range(len(list)):
        num = list[i]
        if num > pivot:
            bigger_nums.append(num)
        elif num < pivot:
            smaller_nums.append(num)
        else:
            pivot_nums.append(pivot)
    return quicksort(smaller_nums) + pivot_nums + quicksort(bigger_nums)


list_length = 1000000
unordered_list = random.sample(range(0, 1*list_length), list_length)

start = time.time()
ordered_list = quicksort(unordered_list)
end = time.time()

print(ordered_list)
print(end-start)

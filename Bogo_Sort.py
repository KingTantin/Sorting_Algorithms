import random
import time

def bogo_sort(unordered_list: list[int]) -> list[int]:
    while True:
        is_sorted = True
        random.shuffle(unordered_list)

        for i in range(0, len(unordered_list)-1):
            if unordered_list[i] > unordered_list[i+1]:
                is_sorted = False
                break

        if is_sorted == True:  
            print(unordered_list)
            break
    return unordered_list


#Generate list_length random numbers between 1 and listh_length+1
list_length = 9
unordered_list = random.sample(range(1, 2*list_length), list_length)

start = time.time()
ordered_list = bogo_sort(unordered_list)
end =  time.time()

print(ordered_list)
print(end-start)

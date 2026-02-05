import random
import time
from collections import deque
#Generate list_length random numbers between 1 and listh_length+1

def selection_sort(unordered_list: list) -> list:

    ordered_list_1 = []
    ordered_list_2 = deque()
    ordered_list = deque()

    for x in range(int(len(unordered_list)/2)):
        lowest_number = unordered_list[0]
        highest_number = unordered_list[0]

        for i in range(1, len(unordered_list)):
            if lowest_number > unordered_list[i]:
                lowest_number = unordered_list[i]
            if highest_number < unordered_list[i]:
                highest_number = unordered_list[i]
                
        unordered_list.remove(lowest_number)
        unordered_list.remove(highest_number)
        ordered_list_1.append(lowest_number)
        ordered_list_2.appendleft(highest_number)
        
    ordered_list = ordered_list_1 + ordered_list_2
    return ordered_list



list_length = 10000
unordered_list = random.sample(range(1, 2*list_length), list_length)

start = time.time()
ordered_list = selection_sort(unordered_list)
end = time.time()

print(ordered_list)
print(end - start)

#Time Complexity = O(  (n/2)**2  ) which simplified to O(n**2)
#Selection Sort

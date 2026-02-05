import random
import time

def insertion_sort(unorderd_list: list) -> list:
    ordered_list = [unordered_list[0]]
    for i in range(1, len(unordered_list)):
        if ordered_list[i-1] < unordered_list[i]:
            ordered_list.append(unordered_list[i])
            
            
        else:
            left = 0
            right = len(ordered_list)
            while right >= left:
                
                mid = int((right + left)/2)
                
                if ordered_list[mid] > unordered_list[i]:
            
                    right = mid - 1
                    
                elif ordered_list[mid] < unordered_list[i]:
                    left = mid+1
                else:
                    ordered_list.insert(mid, unordered_list[i])
                    break
            ordered_list.insert(left, unordered_list[i])



    return ordered_list

list_length = 10000
unordered_list = random.sample(range(1, 2*list_length), list_length)

start = time.time()
ordered_list = insertion_sort(unordered_list)
end = time.time()

print(ordered_list)
print(end-start)

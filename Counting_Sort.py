import random
import time

#problems no floating point numbers and if lowest_number and highest_number are far apart it is slow
def counting_sort(unordered_list: list[int]) -> list[int]:
    diction = {}
    ordered_list = []
    seen = set()
    duplicate = {}

    highest_number = unordered_list[0]
    lowest_number = unordered_list[0]
    for i in unordered_list:
        diction[i] = i
        if highest_number < i:
            highest_number = i
        if lowest_number > i:
            lowest_number = i

        if i not in seen:
            seen.add(i)
            duplicate[i] = 1
        else:
            duplicate[i] += 1


    for i in range(int(lowest_number), int(highest_number)+1):            
        try:
            for x in range(duplicate[i]):
                ordered_list.append(diction[i])
        except KeyError:
            ""

    return ordered_list


list_length = 1000000
unordered_list = random.sample(range(0, 1*list_length), list_length)

start = time.time()
ordered_list = counting_sort(unordered_list)
end = time.time()

print(ordered_list)
print(end-start)

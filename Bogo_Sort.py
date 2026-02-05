import random
import time
#Generate list_length random numbers between 1 and listh_length+1
list_length = 10
unordered_list = random.sample(range(1, 2*list_length), list_length)

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
start = time.time()
bogo_sort(unordered_list)
end =  time.time()
print(end-start)

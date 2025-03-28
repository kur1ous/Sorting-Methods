import random 
import time

def create_list(n):
    return [i for i in range (n)]



def shuffle(list):
    for i in range(len(list)):
        random_index = random.randint(0, len(list) - 1)
        swap = list[i]
        list[i] = list[random_index]
        list[random_index] = swap


def sort_toggle(list):
    if len(list) <= 1: return True
    for i in range(1, len(list)):
        if list[i-1] > list[i]:
            return False
    return True

def bozo_sort(list): # don't use this LOL
    while not sort_toggle(list):
        shuffle(list)
    return(list)


def bubble_sort(list): # we're getting better
    swapped = True
    while swapped: 
        swapped = False
        for i in range(0, len(list)-1):
            if list[i+1] < list[i]:
                swap = list[i]
                list[i] = list[i+1]
                list[i+1] = swap
                swapped = True


def merge(list1, list2):
    list1 = []
    list2 = []
    

swapped = True


my_list = create_list(1000)

assert(sort_toggle(my_list))
shuffle(my_list)


print(f'Sorting.. {my_list}')

start_time = time.time()
bubble_sort(my_list)
end_time = time.time()




print(f'Sorted List: {my_list}')
print(f'Took {end_time-start_time} seconds')
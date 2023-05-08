#   Instruction types
    #   0: Comp
    #   1: Swap
    #   3: Done

def quick_sort_alg(arr, instructions):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for x in arr[1:]:
            if compare(x, pivot, arr, instructions):
                less.append(x)
            else:
                greater.append(x)
        return quick_sort_alg(less, instructions) + [pivot] + quick_sort_alg(greater, instructions)

def bubble_sort_alg(arr, instructions):
    for num_of_sorted in range(len(arr)):
        for j in range(len(arr)-num_of_sorted-1):
            compare(arr[j], arr[j+1], arr, instructions)


def compare(x, y, arr, instructions = []):
    """
        Returns true if x <= y
        Returns false AND swaps x and y if x > y
    """
    instructions += [(0, arr.index(x), arr.index(y))]
    if x <= y:
        return True
    else:
        swap(x, y, arr, instructions)
        return False

def swap(x, y, arr, instructions = []):
    instructions += [(1, arr.index(x), arr.index(y))]
    temp = x
    x = y
    y = temp

from random import randint as r_int
def place_x_at_random_index(arr, x):
    r = r_int(0, arr.__len__() -1)
    if(arr[r] == "_"):
        arr[r] = x
    else:
        place_x_at_random_index(arr, x)

def create_array(len):
    numOfShuffles = 10
    arr = []

    for x in range(len):
        arr += ["_"]
    
    for x in range(len):
        place_x_at_random_index(arr, x+1)
            
    return arr


def quick_sort(len):
    """
        This is the funtion used by other modules in the program.
        It takes an integer "len" and returns a tuple containing two lists, 
        1: The shuffled array
        2: A list of instructions from the quicksort algorithm.
    """

    originalArray = create_array(len)
    arr = []
    
    for x in originalArray:
        arr += [x]

    instructions = []


    arr = quick_sort_alg(arr, instructions)
    instructions += [[3]]

    return originalArray, instructions


def bubble_sort(len):
    """
        This is the funtion used by other modules in the program.
        It takes an integer "len" and returns a tuple containing two lists, 
        1: The shuffled array
        2: A list of instructions from the bubblesort algorithm.
    """
    originalArray = create_array(len)
    arr = []
    
    for x in originalArray:
        arr += [x]

    instructions = []


    arr = bubble_sort_alg(arr, instructions)
    instructions += [[3]]

    return originalArray, instructions

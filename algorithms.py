#   Instruction types
    #   0: Comp
    #   1: Swap
    #   3: Done

def quick_sort_alg(arr, instructions):
    if(len(arr) <= 1):
        return arr
    else:
        '''
        less = []
        greater = []
        pivot = arr[-1]

        for element in arr[:-1]:
            if(compare(element, pivot, arr, instructions)):
                less += [element]
            else:
                greater += [element]
        
        arr = less + [pivot] + greater
        
        return quick_sort_alg(less, instructions) + [pivot] + quick_sort_alg(greater, instructions)
        '''
        pivot = arr[-1]
        i = 0
        for j in range(len(arr[:-1])):
            stop_loop = False
            if(compare(arr[j], pivot, arr, instructions)):
                while (stop_loop == False):
                    if(compare(pivot, arr[i], arr, instructions)):
                        swap(arr[i], arr[j], arr, instructions)
                        stop_loop = True
                    else:
                        
                        if(i >= j):
                            stop_loop = True
                        else:
                            i += 1
        if(i < len(arr)-1):
            swap(arr[i+1], pivot, arr, instructions)
        
        return arr, f"pivot: {pivot}", f"indexLess: {i}", f"indexGreater: {j}"
        
        #If the pivot is the smallest element in the array, it will be misplaced as the next-smallest




def bubble_sort_alg(arr, instructions):
    for num_of_sorted in range(len(arr)):
        for j in range(len(arr)-num_of_sorted-1):
            if(not compare(arr[j], arr[j+1], arr, instructions)):
                swap(arr[j], arr[j+1], arr, instructions)


def compare(x, y, arr, instructions = []):
    """
        Returns true if x <= y
        Returns false if x > y
    """
    instructions += [(0, arr.index(x), arr.index(y))]
    if x <= y:
        return True
    else:
        return False

def swap(x, y, arr, instructions = []):
    index_x, index_y = arr.index(x), arr.index(y)
    instructions += [(1, index_x, index_y)]
    temp = x
    arr[index_x] = y
    arr[index_y] = temp

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

    return originalArray, instructions, arr


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

print(quick_sort(10))
import random
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

def compare(x, y, arr, instructions = []):
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

def place_x_at_random_index(arr, x):
    r = random.randint(0, arr.__len__() -1)
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
        place_x_at_random_index(arr, x)
            
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

    instructions += [(3)]
    return originalArray, instructions


def bobble_sort(i):
    return ([9,7,5,3,1,8,6,4,2],[[0,0,1],[0,1,2],[1,1,2],[0,2,3],[1,2,3], [3]])
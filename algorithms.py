#   Instruction types
    #   0: Comp
    #   1: Swap
    #   3: Done

def quick_sort_alg(arr, instructions):
    if(len(arr) <= 1):
        return arr
    else:
        pivot = arr[-1]
        i = 0

        # Check if pivot is the smallest element
        pivot_is_smallest = True
        for k in arr:
            if(k < pivot):
                pivot_is_smallest = False
                break
        if(pivot_is_smallest):
            swap(pivot, arr[0], arr, instructions)
            greater = quick_sort_alg(arr[1:], instructions)
            return [pivot] + greater

        for j in range(len(arr[:-1])):
            if(compare(arr[j], pivot, arr, instructions)):
                while (True):
                    if(compare(pivot, arr[i], arr, instructions)):
                        swap(arr[i], arr[j], arr, instructions)
                        break
                    else:
                        if(i >= j):
                            break
                        else:
                            i += 1

        swap(arr[i+1], pivot, arr, instructions)

        less = quick_sort_alg(arr[:arr.index(pivot)], instructions)
        greater = quick_sort_alg(arr[arr.index(pivot)+1:], instructions)
        return less + [pivot] + greater




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
    instructions += [(0, x, y)]
    if x <= y:
        return True
    else:
        return False

def swap(x, y, arr, instructions = []):
    print(x, y)
    
    index_x, index_y = arr.index(x), arr.index(y)
    instructions += [(1, x, y)]
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

    original_array = create_array(len)
    arr = []
    
    for x in original_array:
        arr += [x]

    instructions = []


    arr = quick_sort_alg(arr, instructions)
    instructions += [[3]]

    return original_array, reformat_instructions(original_array, instructions) #, arr


def bubble_sort(len):
    """
        This is the funtion used by other modules in the program.
        It takes an integer "len" and returns a tuple containing two lists, 
        1: The shuffled array
        2: A list of instructions from the bubblesort algorithm.
    """
    original_array = create_array(len)
    arr = []
    
    for x in original_array:
        arr += [x]

    instructions = []


    arr = bubble_sort_alg(arr, instructions)
    instructions += [[3]]

    return original_array, reformat_instructions(original_array, instructions)

def reformat_instructions(original_array, instructions):
    # print(f"imputted instructions: {instructions}")
    new_array = original_array[:]
    new_instructions = []
    for inst in instructions:
        if(inst[0] == 0):
            new_instructions += [(0, new_array.index(inst[1]), new_array.index(inst[2]))]
        elif(inst[0] == 1):
            new_instructions += [(1, new_array.index(inst[1]), new_array.index(inst[2]))]

            index1 = new_array.index(inst[1])
            index2 = new_array.index(inst[2])

            new_array[index1], new_array[index2] = new_array[index2], new_array[index1]

            # print (f"New arr: {new_array}")
    new_instructions.append([3])
    return new_instructions

# for _ in range (1):
#     res = quick_sort(5)
#     print(res[0], res[2], res[1])

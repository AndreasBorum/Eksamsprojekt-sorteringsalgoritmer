"""


(start_data, instruktioner)

start_data = ( 2, 5, 1, 3, 7, 8, 9, x, x)


instruktioner ((type, i1, i2), (type, i1, i2))

typer:
1- sammenlign 
2- byt 
3- færdig



"""
instructions = []

def quicksort(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for x in arr[1:]:
            if compare(x, pivot):
                less.append(x)
            else:
                greater.append(x)
        return quicksort(less) + [pivot] + quicksort(greater)

def compare(x, y):
    instructions += [(1, x, y)]
    if x <= y:
        return True
    else:
        swap(x, y)
        return False

def swap(x, y):
    instructions += [(2, x, y)]
    temp = x
    x = y
    y = temp

# example usage
arr = [4, 7, 1, 8, 5, 2, 6, 3]

quicksort(arr)
print(arr)
print(instructions)



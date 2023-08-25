import random

class Sorting:
    def bubblesort(arr):
        for i in range(len(arr)-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    swap(arr, j, j+1)
        print(arr)

    def selectionsort(arr):
        for i in range(len(arr)-1, 0, -1):
            max = 0
            for j in range(1, i+1):
                if arr[j] > arr[max]:
                    max = j
            swap(arr, max, i)
        print(arr)

    def insertionsort(arr):
        for i in range(1, len(arr)):
            current = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > current:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = current
        print(arr)

    def mergesort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            Sorting.mergesort(left)
            Sorting.mergesort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        print(arr)

    def bogosort(arr):
        while not isSorted(arr):
            for i in range(len(arr)):
                r = random.randint(0, len(arr)-1)
                swap(arr, i, r)
        print(arr)

def isSorted(arr):
    # check if arr is sorted
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# ask user for sorting algorithm
algorithms = [func for func in dir(Sorting) if not func.startswith('__')]
print("Choose a sorting algorithm:")
for i in range(len(algorithms)):
    print(str(i+1) + ". " + algorithms[i])
choice = int(input("Enter a number: "))
if choice < 1 or choice > len(algorithms):
    print("Invalid choice")
    exit()
else: 
    print("You chose " + algorithms[choice-1])
    print("Enter a list of numbers separated by spaces:")
    arr = [int(x) for x in input().split()]
    eval("Sorting." + algorithms[choice-1] + "(arr)")



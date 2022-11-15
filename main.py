import math

# WHAT IS BIG?

# Big O(n) Function
def linearFunction(arr):
    for i in range(len(arr)):
        print(1000 * 100000) # constant time

arr = [1, 2, 3, 4, 5, 6, 7]
# linearFunction(arr)


# Big O(1)
def constantFunc(arr):
    print(1000 * 100000)



# O(n^2)
def square(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# square(4)


# O(n^3)

def cube(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

# O(logn)

# Recursive Example
n = 8
def logFunc(n):
    if n == 0:
        return "Done"
    n = math.floor(n/2)
    return logFunc(n)

# Iterative Example

def logn(n):
    while n > 1:
        n = math.floor(n/2)


# Binary Search and O(logn)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(arr) - 1
target = 10

def binarySearch(arr, start, end, target):
    if start > end: # base case for our recursion
        return False
    mid = (start + end) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binarySearch(arr, start, mid-1, target)
    else:
        return binarySearch(arr, mid+1, end, target)

# print(binarySearch(arr, start, end, target))

# O(nlogn)
def nLogNFunc(n):
    y = n
    while n > 1: # logn
        n = n //2
        for i in range(0, y): # n
            print(i)

# O(logn) * O(n) -> logn * n -> (n)(logn) -> nlogn
# nLogNFunc(4)


# Merge Sort O(nlogn)

def mergeSort(arr):
    if len(arr) < 2: # if our list has 0 or 1 items then it can be assumed to be sorted
        return arr # simply return our input data
    
    midIndex = len(arr) // 2 # find the middle of the array

    left = arr[:midIndex]
    right = arr[midIndex:]

    return merge(mergeSort(left), mergeSort(right)) # recurse left and right

def merge(left, right):
    if not len(left) or not len(right):
        return left or right
    
    result = []
    i, j = 0, 0

    while len(result) < len(left) + len(right): # runs until the result len is no longer less than right+left
        if left[i] < right[j]: # left value is less than right value
            result.append(left[i])
            i += 1
        else:
            result.append(right[j]) # right value is less than left value 
            j += 1

        if i == len(left) or j == len(right): # when left or right is done we can assume the data is sorted 
            result.extend(left[i:] or right[j:]) # our next step is to merge both lists into a single solution
            break

        # the extends method will add an arrays values to the end of the current array 
    
    return result

# data = [12, 11, 13, 5, 6, 7]
# print('data unsorted:', data)
# print('sorted data:', mergeSort(data))

'''
By recursively splitting our data in halves we get O(logn) complexity
iterating to rebuild those arrays we get a complexity of O(n)

O(n) * O(logn) => O(nlogn) Time Complexity
'''
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

print(binarySearch(arr, start, end, target))
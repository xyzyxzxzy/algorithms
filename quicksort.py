# Sort the given array. Use quick sort. O(n * log n)
import random

a = int(input())
n = [random.randint(1, 80) for _ in range(0, a)]

def qsort(arr:list) -> list:
    # base case
    if len(arr) < 2:
        return arr

    # pivot element
    pivot = arr[len(arr) // 2]
    greater, less = [], []

    for i in arr:
        if i == pivot:
            continue

        if i > pivot: # all array elements are greater than pivot
            greater.append(i)
        else: #all array elements are less than pivot
            less.append(i)

    return qsort(less) + [pivot] + qsort(greater)

print(qsort(n))

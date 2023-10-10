# In the first line, enter one natural number,
# not exceeding 1000 – array size. The second line specifies
# N numbers – array elements (integers not exceeding modulo 1000). O(n^2)

a = int(input())
n = [int(input()) for _ in range(0, a)]

# looking for the smallest element in the array
def findSmallest(arr:list) -> int:
    smallest_index = 0
    smallest = arr[smallest_index]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index

def selectionSort(arr:list) -> list:
    newArr = []
    for i in range(len(arr)):
        newArr.append(arr.pop(findSmallest(arr)))

    return newArr

print(selectionSort(n))

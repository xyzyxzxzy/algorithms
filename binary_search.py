# For each of the K numbers, it is required to print “YES” in a separate line
# if this number is found in the first array, and “NO” otherwise.

import random
from typing import Optional

n = [random.randint(1, 80) for _ in range(0, 10)]
k = [random.randint(1, 80) for _ in range(0, 10)]
k.sort()
print(n)
print(k)

def search_number_binary(n:list, needle:int) -> Optional[int]:
    low = 0
    high = len(n) - 1

    while low <= high:
        middle = round((low + high) / 2)
        if n[middle] == needle:
            return middle

        if n[middle] < needle:
            low = middle + 1

        if n[middle] > needle:
            high = middle - 1

    return None


for i in range(0, len(k)):
    index = search_number_binary(n, k[i])

    if index == None:
        print(f"{k[i]} - NO")
        continue
    print(f"{k[i]} - YES")

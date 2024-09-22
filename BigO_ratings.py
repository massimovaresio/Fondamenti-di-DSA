"""Esercizio: assegnare ad ogni script un valutazione riguardo alla complessità algoritmica con notazione Big O
"""

# Esercizio 1
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
# Complessità: O(n)

# Esercizio 2
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
# Complessità: O(n)

# Esercizio 3
def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])
# Complessità: O(n^2)

# Esercizio 4
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Complessità: O(log(n))


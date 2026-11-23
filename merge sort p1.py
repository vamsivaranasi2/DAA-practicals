import time

def mergeSort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1

arr = []

n = int(input("Enter the number of elements: "))

print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

print("Original Array:", arr)

start = time.time()

mergeSort(arr)

end = time.time()

print("Sorted Array:", arr)
print("Time taken:", end - start, "seconds")

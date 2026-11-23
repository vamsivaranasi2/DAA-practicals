import time

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right

arr = []
n = int(input("Enter the number of elements: "))

print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

print("Original Array:", arr)

start = time.time()

arr = quickSort(arr)

end = time.time()

print("Sorted Array:", arr)
print("Time taken:", end - start, "seconds")


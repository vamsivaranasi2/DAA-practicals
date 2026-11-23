import time
arr = []
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(n):
    value = int(input())
    arr.append(value)
print("Original Array:", arr)
start = time.time()
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            print("Swapping", arr[j], "and", arr[j + 1])
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            print("Array after swap:", arr)
end = time.time()
print("Sorted Array:", arr)
print("Time taken:", end - start, "seconds")
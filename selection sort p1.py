import time
arr = []
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

print("Original Array:", arr)

start = time.time()

for i in range(n):
    minIndex = i
    for j in range(i + 1, n):
        if arr[j] < arr[minIndex]:
            minIndex = j

    if minIndex != i:
        print("Swapping", arr[i], "and", arr[minIndex])
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
        print("Array after swap:", arr)

end = time.time()

print("Sorted Array:", arr)
print("Time taken:", end - start, "seconds")


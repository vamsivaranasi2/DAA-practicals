import time

arr = []
n = int(input("Enter the number of elements: "))

print("Enter the sorted elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

start = time.time()

first = 0
last = n - 1

while first <= last:
    mid = (first + last) // 2

    if arr[mid] == key:
        print("Element found at position", mid + 1)
        break
    elif key < arr[mid]:
        last = mid - 1
    else:
        first = mid + 1

end = time.time()

if first > last:
    print("Element not found")

print("Time taken:", end - start, "seconds")

import time

arr = []
n = int(input("Enter the number of elements: "))

print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

key = int(input("Enter the element to search: "))

start = time.time()

flag = 0
for i in range(n):
    if arr[i] == key:
        print("Element found at position", i + 1)
        flag = 1
        break

end = time.time()

if flag == 0:
    print("Element not found")

print("Time taken:", end - start, "seconds")


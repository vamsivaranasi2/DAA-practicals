import time 
arr = [] 
n = int(input("Enter the number of elements: ")) 
print("Enter the elements:") 
for i in range(n): 
    num = int(input()) 
    arr.append(num) 
print("Original Array:", arr) 
start = time.time()
for i in range(1, n): 
    current = arr[i] 
    j = i - 1 
    while j >= 0 and arr[j] > current: 
        print("Moving", arr[j], "to the next position") 
        arr[j + 1] = arr[j] 
        j = j - 1 
    arr[j + 1] = current 
    print("Array after pass", i, ":", arr) 
end = time.time()
print("Sorted Array:", arr) 
print("Time taken:", end - start, "seconds")
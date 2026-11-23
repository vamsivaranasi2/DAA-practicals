import time

heap = []

n = int(input("Enter number of elements: "))
print("Enter the elements:")

for i in range(n):
    heap.append(int(input()))

start = time.time()

for i in range(n // 2 - 1, -1, -1):
    parent = i

    while True:
        left = 2 * parent + 1
        right = 2 * parent + 2
        largest = parent

        if left < n and heap[left] > heap[largest]:
            largest = left

        if right < n and heap[right] > heap[largest]:
            largest = right

        if largest == parent:
            break

        heap[parent], heap[largest] = heap[largest], heap[parent]
        parent = largest

end = time.time()

print("Max Heap:", heap)
print("Time taken:", end - start, "seconds")
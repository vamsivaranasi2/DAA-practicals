import time

number = int(input("Enter a number: "))

factorial = 1
step = 0

if number < 0:
    print("Factorial is not possible for negative numbers")
else:
    start = time.time()

    value = 1

    while value <= number:
        factorial = factorial * value
        step = step + 1
        value = value + 1

    end = time.time()

    print("Factorial of", number, "is", factorial)
    print("Steps performed:", step)
    print("Logic Used: Repeated multiplication using a loop")
    print("Time Complexity: O(n)")
    print("Time taken:", end - start, "seconds")
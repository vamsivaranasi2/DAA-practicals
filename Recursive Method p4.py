import time

step = 0

def find_factorial(number):
    global step
    step = step + 1

    if number == 0 or number == 1:
        return 1

    return number * find_factorial(number - 1)

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not possible for negative numbers")
else:
    start = time.time()

    answer = find_factorial(number)

    end = time.time()

    print("Factorial of", number, "is", answer)
    print("Steps performed:", step)
    print("Logic Used: Function calls itself until it reaches 1")
    print("Time Complexity: O(n)")
    print("Time taken:", end - start, "seconds")
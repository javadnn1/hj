n = int(input(''))
def factorial(n):
    if n == 0:
        return 1
    if n > 10:
        return "Number out of range"
    if n > 0:
        return n * factorial(n-1)

if 1 <= n <= 10:
    print(f"The factorial of {n} is {factorial(n)}")
else:
    print("Please enter a number between 1 and 10")
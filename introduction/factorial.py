# factorial code
# 5! = 5 * 4 * 3 * 2 * 1
# 5 * (5-1) * (5-2) * (5-3) * (5-4)

def factorial(n):
    if n > -1 and n < 1:
        return 1
    elif n < 0:
        return None
    product = 1
    for i in reversed(range(1, n+1)):
        product *= i
    return product

print(factorial(-1))
# iterative fibonacci sequence
# bottom-up approach

def fibonacci(n):
    if n <= 1:
        return n
    fib_arr = [0] * (n+1)
    fib_arr[1] = 1
    for i in range(2, (n+1)):
        fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]
    return fib_arr[n]
print(fibonacci(8))
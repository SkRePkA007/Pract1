def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Вивід перших 40 чисел Фібоначчі
fib_sequence = fibonacci(40)
for num in fib_sequence:
    print(num)

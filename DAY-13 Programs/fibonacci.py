def nth_fibonacci_number(n):
    if n == 1 or n == 2:
        return 1
    return nth_fibonacci_number(n - 1) + nth_fibonacci_number(n - 2)

def sum_till_nth(n):
    total = 0
    for i in range(1, n + 1):
        total += nth_fibonacci_number(i)
    return total

n = 10
print("The", n, "Fibonacci number is:", nth_fibonacci_number(n))
print("The sum of Fibonacci numbers up to", n, "is:", sum_till_nth(n))
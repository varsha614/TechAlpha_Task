def fibonacci_generator(N):
    fibonacci_sequence = [0, 1]
    for i in range(2, N):
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence
N = int(input("Enter a number: "))
fibonacci_sequence = fibonacci_generator(N)
print("Fibonacci sequence up to the", N, "th term:")
print(fibonacci_sequence)

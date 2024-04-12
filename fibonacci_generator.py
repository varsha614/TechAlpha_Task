def fibonacci_generator(n):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers
    
    # Generate Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    
    return fibonacci_sequence

n = int(input("Enter a number: "))
fibonacci_sequence = fibonacci_generator(n)
print("Fibonacci sequence up to the", n, "th term:")
print(fibonacci_sequence)

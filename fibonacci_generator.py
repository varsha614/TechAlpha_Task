def fibonacci_generator(n):
    prevNum = 0
    currentNum = 1
    for i in range(1, n):
        prevprevNum = prevNum
        prevNum = currentNum
        currentNum = prevNum + prevprevNum
    return currentNum

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Fibonacci sequence up to the {num} th number: {fibonacci_generator(num)}")
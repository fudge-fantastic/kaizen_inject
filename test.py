def generate_fibonacci(limit):
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] < limit:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

if __name__ == "__main__":
    limit = int(input("Enter the limit: "))
    fibonacci = generate_fibonacci(limit)
    print("Fibonacci sequence up to {}: {}".format(limit, fibonacci))
    
# -u origin main
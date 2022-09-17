def fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return fibonacci(idx - 1) + fibonacci(idx - 2)

print(fibonacci(5))
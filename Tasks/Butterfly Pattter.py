# Function to print the butterfly pattern
def butterfly_pattern(n):
    # Upper part of the butterfly
    for i in range(1, n + 1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)

    # Lower part of the butterfly
    for i in range(n, 0, -1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Number of rows for each half of the butterfly
rows = 6
butterfly_pattern(rows)

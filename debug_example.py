def compute_ratio(a, b):
    if b == 0:
        return 0  # Avoid ZeroDivisionError
    return a / b

def main():
    values = [1, 2, 3, 0, 4]
    total = 0
    for v in values:
        try:
            total += compute_ratio(10, v)
        except ZeroDivisionError:
            print(f"Cannot divide by zero for value: {v}")
    print("Total:", total)

if __name__ == "__main__":
    main()

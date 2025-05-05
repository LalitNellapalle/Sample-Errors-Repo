def add_numbers(a, b):
    # Type error: Trying to add a string and a number
    return a + b

def process_data(data):
    # Type error: Treating a non-iterable as iterable
    for item in data:
        print(item)

def calculate_average(numbers):
    # Type error: Dividing by a string
    total = sum(numbers)
    count = "5"  # This should be an integer
    return total / count

# Demo function with type errors
def main():
    # This will cause a type error
    result = add_numbers(5, "10")
    print(result)
    
    # This will cause a type error
    process_data(123)
    
    # This will cause a type error
    avg = calculate_average([1, 2, 3, 4, 5])
    print(avg)

if __name__ == "__main__":
    main()
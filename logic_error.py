def is_prime(n):
    # Logic error: Incorrect prime number check
    if n <= 1:
        return False
    for i in range(2, n):  # Should be range(2, int(n**0.5) + 1)
        if n % i == 0:
            return False
    return True

def find_largest(numbers):
    # Logic error: Incorrect way to find the largest number
    largest = 0  # Should initialize to numbers[0] or float('-inf')
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def calculate_discount(price, discount_percent):
    # Logic error: Incorrect discount calculation
    discount = price * discount_percent  # Should be price * (discount_percent / 100)
    return price - discount

# Demo function with logic errors
def main():
    # This will incorrectly identify 9 as a prime number
    print(f"Is 9 prime? {is_prime(9)}")
    
    # This will return incorrect result for all negative numbers
    print(f"Largest number: {find_largest([-5, -10, -3])}")
    
    # This will apply the wrong discount
    print(f"Discounted price: {calculate_discount(100, 20)}")

if __name__ == "__main__":
    main()
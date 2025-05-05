def process_items(items):
    # Index out of bounds error: Trying to access an index that doesn't exist
    first_item = items[0]  # Error if items is empty
    
    # Another index error when processing a list
    for i in range(len(items) + 1):  # The +1 will cause index error on the last iteration
        print(f"Processing item: {items[i]}")
    
    return True

def get_matrix_element(matrix, row, col):
    # Index error in 2D array access
    return matrix[row][col]  # Potential error if row or col is out of bounds

# Demo function with potential index error
def main():
    sample_list = [1, 2, 3]
    process_items(sample_list)
    
    # This will cause an index error
    print(sample_list[5])
    
    matrix = [[1, 2], [3, 4]]
    # This might cause an index error
    print(get_matrix_element(matrix, 2, 0))

if __name__ == "__main__":
    main()
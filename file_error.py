def read_file_contents(filename):
    # File error: Opening a file without proper error handling
    f = open(filename, 'r')
    content = f.read()
    # Missing f.close() - resource leak
    return content

def write_to_file(filename, content):
    # File error: Writing to a file without proper error handling
    f = open(filename, 'w')
    f.write(content)
    # Missing f.close() - resource leak
    return True

def append_to_log(log_file, message):
    # File error: Trying to write to a file that might not exist
    with open(log_file, 'a') as f:
        f.write(message + "\n")

# Demo function with file errors
def main():
    # This might cause a file not found error
    content = read_file_contents("non_existent_file.txt")
    print(content)
    
    # This might not close the file properly
    write_to_file("output.txt", "Some content")
    
    # This might try to write to a protected directory
    append_to_log("/system/logs/app.log", "Test message")

if __name__ == "__main__":
    main()
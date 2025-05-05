#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// Function that creates a memory leak
void memory_leak_example() {
    // Memory is allocated but never freed
    char* buffer = (char*) malloc(100);
    
    // Use the buffer
    strcpy(buffer, "This memory will be leaked");
    printf("Buffer contains: %s\n", buffer);
    
    // No free(buffer) call, so this memory is leaked
}

// Function that creates multiple memory leaks
void multiple_memory_leaks() {
    int* numbers = (int*) malloc(5 * sizeof(int));
    char* text = (char*) malloc(50);
    
    // Use the allocations
    for (int i = 0; i < 5; i++) {
        numbers[i] = i * 10;
    }
    strcpy(text, "More leaked memory");
    
    printf("First number: %d\n", numbers[0]);
    printf("Text: %s\n", text);
    
    // Neither allocation is freed
}

// Function with null pointer error
void null_pointer_example() {
    char* ptr = NULL;
    
    // Attempt to use a NULL pointer
    printf("This will crash: %s\n", ptr);  // Dereferencing NULL
    *ptr = 'A';  // This will also cause a segmentation fault
}

// Function with conditional null pointer error
void conditional_null_pointer() {
    // This function might return NULL in real code
    char* data = getenv("NONEXISTENT_VARIABLE");
    
    // Failure to check for NULL before using
    printf("Length of data: %lu\n", strlen(data));  // Will crash if data is NULL
}

int main() {
    printf("Starting error examples program\n");
    
    // Call the memory leak functions
    memory_leak_example();
    multiple_memory_leaks();
    
    printf("Memory leak examples completed\n");
    
    // Uncomment to test null pointer errors (will crash the program)
    // null_pointer_example();
    // conditional_null_pointer();
    
    printf("Program completed successfully\n");
    return 0;
}
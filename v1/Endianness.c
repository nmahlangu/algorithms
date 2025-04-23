// Write a function in C that distinguishes the endianness of the architecture. It should return
// true in one case and false in the other.

#include <stdio.h>
#include <stdlib.h>

int big_endian(void){
    uint32_t x = 1;
    char* p = (char*)&x;
    return *p;
}

int main(void){
    if (big_endian()){
        printf("System is big endian\n");
    }
    else {
        printf("System is little endian\n");
    }
}

// Solution: Create an unsigned 32-bit integer and initialize it to 1. Then, create
// a char* and point it to the address of this integer (don't forget to cast it
// to a char*). If the system is big endian, the value in memory at this pointer
// will be 1. If the system is little endian, the value will be 0.

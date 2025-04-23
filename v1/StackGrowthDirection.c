// Determine if a system's stack grows up or down in the memory address space
// using C code.

#include <stdio.h>
#include <stdlib.h>

int main(void){
    int x;
    int y;
    if (&x < &y)
        printf("Stack grows from lower to higher memory addresses\n");
    else
        printf("Stack grows from higher to lower memory addresses\n");
}

// Solution: Declare 2 variables in the same stack frame. If the latter
// one has a lower address, the stack grows downwards in the memory space.
// If the former one has a lower address, the stack grows upwards in the
// memory space.

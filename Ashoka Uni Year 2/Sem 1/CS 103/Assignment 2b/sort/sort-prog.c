#include <stdio.h>
#include <stdlib.h>

// Create a short form for 64-bit integer
typedef unsigned long long uint64_t;

// Function to take the base address and the number of elements of an
// array and  sort  all the elements

void sort(uint64_t *, uint64_t);


// Main function - entry point for the program

int main(int argc, char **argv) {

  uint64_t count;
  uint64_t *a;

  // read the number of elements in the array
  if (fscanf(stdin, "%llu", &count)) {};

  // allocate space for the array
  a = (uint64_t *) malloc(sizeof(uint64_t) * count);

  // read all the elements of the array
  for (uint64_t i = 0; i < count; i ++) {
    if(fscanf(stdin, "%llu", &a[i])) {};
  }

  // compute the sort
  sort(a, count);

  // print the result
  for (uint64_t i = 0; i < count; i ++) {
    fprintf(stdout, "%llu\n", a[i]);
  }

  // return
  return 0;
}

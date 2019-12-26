#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

int main() {

  int a[1024][1024];

  // randomly initialize the array
  for (int i = 0; i < 1024; i ++) {
    for (int j = 0; j < 1024; j ++) {
      a[i][j] = rand();
    }
  }

  // time boundaries
  struct timeval start, end;

  int sum = 0;
  long long total_time = 0;
  for (int iter = 0; iter < 1000; iter ++) {

    // main loop to measure
    gettimeofday(&start, NULL);

    for (int i = 0; i < 1024; i ++) {
      for (int j = 0; j < 1024; j ++) {
	sum += a[i][j];
      }
    }
    
    gettimeofday(&end, NULL);
    
    // compute how much time it took
    long long diff = (end.tv_sec * 1000000 + end.tv_usec)
      - (start.tv_sec * 1000000 + start.tv_usec);
    total_time += diff;
  }

  total_time /= 1000;

  // print the sum and time
  printf("Sum = %d\nTime = %lld us\n", sum, total_time);

  return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

int main() {
	
	FILE *time_splits= fopen("splits.txt","w"); //file to record the time and array size
	struct timeval start, stop;
		
	for (int j=1;j<=32768;j++) //main loop
	{
		int n=512*j; //n is assigned here
		
		int *a=malloc(n*sizeof(int)); //allocates memory for first array
		int *b=malloc(n*sizeof(int)); //allocates memory for second array
		int *sum=malloc(n*sizeof(int)); //allocates memory for sum array
		
		for (int i=0;i<n;i++) //loop to give a and b random values
		{
			a[i]=rand();
			b[i]=rand();
		}
		
		gettimeofday(&start, NULL); //notes start time
		
		for (int i=0;i<n;i++) //adding loop
		{
			sum[i]=a[i]+b[i];
		}
		
		gettimeofday(&stop, NULL); //notes ending time
		
		double time_taken = ((stop.tv_sec * 1000000 + stop.tv_usec)- (start.tv_sec * 1000000 + start.tv_usec))/1000; //final time taken
		
		printf("%f,%d",time_taken,n);
		fprintf(time_splits,"%f , %d\n",time_taken,n);
		fprintf(time_splits,"\r\n");
		
		free(a);
		free(b);
		free(sum);		
		
	}
	fclose(time_splits);
	
  return 0;
}

//Divij Singh
//Assignment 4 for CS 103
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

int n=32;
int i;
int j;
int k;
int x;
double time_taken;
double FLOPS;
int a[2048][2048];
int b[2048][2048];
int c[2048][2048];
double cube=0;


int main()
{
	clock_t time_check;

	for (i=0;i<2048;i++) //loop to give a and b random values
	{
		for(j=0;j<2048;j++)
		{
			a[i][j]=rand();
			b[i][j]=rand();
		}
	}

	for(x=1;x<5;x++)
	{

		for (i = 0; i < n; i ++) //ordering 1 run 1
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[i][j] += a[i][k] * b[k][j];
    			}
    		}
    	}

    	time_check=clock(); //notes start time

    	for (i = 0; i < n; i ++) //ordering 1 run 2
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[i][j] += a[i][k] * b[k][j];
    			}
    		}
    	}

    	time_taken = (double)(clock()-time_check)/CLOCKS_PER_SEC; //final time taken

    	cube=n*n;
    	cube=cube*n*2;

    	FLOPS =(double)(cube/time_taken);

    	printf("1 , %d , %lf , %d\n",x,FLOPS,n);
    	printf("\r\n");

    	for (i = 0; i < n; i ++) //ordering 2 run 1
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[j][i] += a[j][k] * b[k][i];
    			}
    		}
    	}

    	time_check=clock(); //notes start time

    	for (i = 0; i < n; i ++) //ordering 2 run 2
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[j][i] += a[j][k] * b[k][i];
    			}
    		}
    	}

    	time_taken = (double)(clock()-time_check)/CLOCKS_PER_SEC; //final time taken

    	cube=n*n;
    	cube=cube*n;
    	FLOPS =(double)(2*cube)/(time_taken);

    	printf("2 , %d , %lf , %d\n",x,FLOPS,n);
    	printf("\r\n");

    	for (i = 0; i < n; i ++) //ordering 3 run 1
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[k][j] += a[k][i] * b[i][j];
    			}
    		}
    	}

    	time_check=clock(); //notes start time

    	for (i = 0; i < n; i ++) //ordering 3 run 2
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[k][j] += a[k][i] * b[i][j];
    			}
    		}
    	}

    	time_taken = (double)(clock()-time_check)/CLOCKS_PER_SEC; //final time taken

    	cube=n*n;
    	cube=cube*n;
    	FLOPS =(double)(2*cube)/(time_taken);

    	printf("3 , %d , %lf , %d\n",x,FLOPS,n);
    	printf("\r\n");

    	for (i = 0; i < n; i ++) //ordering 4 run 1
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[i][k] += a[i][j] * b[j][k];
    			}
    		}
    	}

    	time_check=clock(); //notes start time

    	for (i = 0; i < n; i ++) //ordering 4 run 2
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[i][k] += a[i][j] * b[j][k];
    			}
    		}
    	}

    	time_taken = (double)(clock()-time_check)/CLOCKS_PER_SEC; //final time taken

    	cube=n*n;
    	cube=cube*n;
    	FLOPS =(double)(2*cube)/(time_taken);

    	printf("4 , %d , %lf , %d\n",x,FLOPS,n);
    	printf("\r\n");

    	for (i = 0; i < n; i ++) //ordering 5 run 1
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[k][i] += a[k][j] * b[j][i];
    			}
    		}
    	}

    	time_check=clock(); //notes start time

    	for (i = 0; i < n; i ++) //ordering 5 run 2
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[k][i] += a[k][j] * b[j][i];
    			}
    		}
    	}

    	time_taken = (double)(clock()-time_check)/CLOCKS_PER_SEC; //final time taken

    	cube=n*n;
    	cube=cube*n;
    	FLOPS =(double)(2*cube)/(time_taken);

    	printf("5 , %d , %lf , %d\n",x,FLOPS,n);
    	printf("\r\n");

    	for (i = 0; i < n; i ++) //ordering 6 run 1
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[k][j] += a[k][i] * b[i][j];
    			}
    		}
    	}

    	time_check=clock(); //notes start time

    	for (i = 0; i < n; i ++) //ordering 6 run 2
    	{
    		for (j = 0; j < n; j ++)
    		{
    			for (k = 0; k < n; k ++)
    			{
    				c[k][j] += a[k][i] * b[i][j];
    			}
    		}
    	}

    	time_taken = (double)(clock()-time_check)/CLOCKS_PER_SEC; //final time taken

    	cube=n*n;
    	cube=cube*n;
    	FLOPS =(double)(2*cube)/(time_taken);

    	printf("6 , %d , %lf , %d\n",x,FLOPS,n);
    	printf("\r\n");

		n=n*4;
	}
	return 0;
}
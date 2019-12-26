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

int i_1;
int i_2=32;

int block00;
int block01;
int block10;
int block11;

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

		for (i_1 = 0; i_1 < n; i_1 += i_2) //set 1 run 1
		{
    		for (i = 0; i < n; i += 2)
    		{
        		for (j = i_1; j < i_1 + i_2; j += 2)
        		{
            		block00 = block01 = block10 = block11 = 0;
            
            		for (k = 0; k < n; k++)
            		{
                		block00 += a[k][j + 0] * b[i + 0][k];
                		block01 += a[k][j + 1] * b[i + 0][k];
                		block10 += a[k][j + 0] * b[i + 1][k];
                		block11 += a[k][j + 1] * b[i + 1][k];
            		}
            		
            		c[i + 0][j + 0] = block00;
            		c[i + 0][j + 1] = block01;
            		c[i + 1][j + 0] = block10;
            		c[i + 1][j + 1] = block11;
       			}
    		}
		}

    	time_check=clock(); //notes start time

    	for (i_1 = 0; i_1 < n; i_1 += i_2) //set 1 run 2
		{
    		for (i = 0; i < n; i += 2)
    		{
        		for (j = i_1; j < i_1 + i_2; j += 2)
        		{
            		block00 = block01 = block10 = block11 = 0;
            
            		for (k = 0; k < n; k++)
            		{
                		block00 += a[k][j + 0] * b[i + 0][k];
                		block01 += a[k][j + 1] * b[i + 0][k];
                		block10 += a[k][j + 0] * b[i + 1][k];
                		block11 += a[k][j + 1] * b[i + 1][k];
            		}
            		
            		c[i + 0][j + 0] = block00;
            		c[i + 0][j + 1] = block01;
            		c[i + 1][j + 0] = block10;
            		c[i + 1][j + 1] = block11;
       			}
    		}
		}
    	

    	time_taken = (double)(clock()-time_check)/CLOCKS_PER_SEC; //final time taken

    	cube=n*n;
    	cube=cube*n*2;

    	FLOPS =(double)(cube/time_taken);

    	printf("1 , %d , %lf , %d\n",x,FLOPS,n);
    	printf("\r\n");

    	for (i_1 = 0; i_1 < n; i_1 += i_2) //set 2 run 1
		{
    		for (i = 0; i < n; i += 2)
    		{
        		for (k = i_1; k < i_1 + i_2; k += 2)
        		{
            		block00 = block01 = block10 = block11 = 0;
            
            		for (j = 0; j < n; j++)
            		{
                		block00 += a[k][j + 0] * b[i + 0][k];
                		block01 += a[k][j + 1] * b[i + 0][k];
                		block10 += a[k][j + 0] * b[i + 1][k];
                		block11 += a[k][j + 1] * b[i + 1][k];
            		}
            		
            		c[i + 0][j + 0] = block00;
            		c[i + 0][j + 1] = block01;
            		c[i + 1][j + 0] = block10;
            		c[i + 1][j + 1] = block11;
       			}
    		}
		}

    	time_check=clock(); //notes start time

    	for (i_1 = 0; i_1 < n; i_1 += i_2) //set 2 run 2
		{
    		for (i = 0; i < n; i += 2)
    		{
        		for (k = i_1; k < i_1 + i_2; k += 2)
        		{
            		block00 = block01 = block10 = block11 = 0;
            
            		for (j = 0; j < n; j++)
            		{
                		block00 += a[k][j + 0] * b[i + 0][k];
                		block01 += a[k][j + 1] * b[i + 0][k];
                		block10 += a[k][j + 0] * b[i + 1][k];
                		block11 += a[k][j + 1] * b[i + 1][k];
            		}
            		
            		c[i + 0][j + 0] = block00;
            		c[i + 0][j + 1] = block01;
            		c[i + 1][j + 0] = block10;
            		c[i + 1][j + 1] = block11;
       			}
    		}
		}
    	

    	time_taken = (double)(clock()-time_check)/CLOCKS_PER_SEC; //final time taken

    	cube=n*n;
    	cube=cube*n*2;

    	FLOPS =(double)(cube/time_taken);

    	printf("2 , %d , %lf , %d\n",x,FLOPS,n);
    	printf("\r\n");

		n=n*4;
	}
	return 0;
}
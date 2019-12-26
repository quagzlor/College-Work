#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {

  int *num_array = (int*)malloc(sizeof(int)*1000);
  char num_str[1000];

  fgets(num_str, 1000, stdin);
  
  char *toke = strtok (num_str," ");
  int i = 0;

  do{
    
    num_array[i++]=atoi(toke);

  }while (toke = strtok(NULL," "));

  int arr_size=i;

  int *max_array = (int*)malloc(sizeof(int)*arr_size);
  int *holder_array = (int*)malloc(sizeof(int)*arr_size);
  int j = 0;
  int counter = 0;
  int max = 0;
  int k=0;

  for(i=0;i<arr_size;i++){
    holder_array[0]=num_array[i];
    counter=1;

    for(j=i+1;j<arr_size;j++){

      if(num_array[j]>holder_array[counter-1]){
        holder_array[counter]=num_array[j];
        counter++;
      }
    
    }
    if(counter>max){

      for(k=0;k<counter;k++){

        max_array[k]=holder_array[k];
      }
      max=counter;
    }
  } 
  for(i=0;i<max;i++){

    printf("%d ",max_array[i]);
  }

  return 0;
  }
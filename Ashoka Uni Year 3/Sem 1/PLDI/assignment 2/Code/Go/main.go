package main

import "fmt"
import "bufio"
import "strings"
import "os"
import "strconv"

func main() {
  i := 0
  j := 0
  k := 0

  reader := bufio.NewReader(os.Stdin)
  input, _ := reader.ReadString('\n')

  fmt.Println()
  input_split := strings.Fields(input)
  input_int := []int{}


  for i = 0;i< len(input_split);i++{
    x, _ := strconv.Atoi(input_split[i])
    input_int=append(input_int,x)
  }

  int_count := i
  max_count := 0
  counter := 0
  var final_int []int
  var hold_int []int
  

  for i = 0; i<int_count; i++{
    hold_int= nil
    hold_int = append(hold_int, input_int[i])
    counter = 1

    for j=(i+1);j<int_count;j++{

      if(input_int[j]>hold_int[counter-1]){
        
        hold_int = append(hold_int, input_int[j])
        counter=counter+1
      }
    }
    if(counter>max_count){

      final_int= nil
      for k=0;k<counter;k++{
        final_int=append(final_int,hold_int[k])
      }
      max_count=counter
      }
    }

  for i=0;i<max_count;i++{
    fmt.Print(final_int[i])
    fmt.Print(" ")
  }
  
}
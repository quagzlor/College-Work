input_arr= input().split()

num_arr=[]

for i in range(len(input_arr)):
  num_arr.append(int(input_arr[i]))

main_array=[]
counter=0

for i in range(0,len(num_arr)):

  temp_arr=[]
  temp_arr.append(int(num_arr[i]))
  counter=1

  for j in range(i+1,len(num_arr)):

    if(num_arr[j]>temp_arr[counter-1]):

      temp_arr.append(num_arr[j])
      counter=counter+1

  if(counter>len(main_array)):

    main_array=temp_arr
    
print (main_array)
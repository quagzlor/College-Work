#Divij Singh
#Note: My CPU has 8 cores. Adjust this to your number of cores
import time #for timing the process
import random #for random values for the array
import multiprocessing #for getting the cores
from threading import Thread #for splitting the program into threads

parallel_sum_arr=[0]*8 #array to store the result from each thread

def main(): #main method. when running in IDLE, start program then type main() and press enter

	serial_sum = 0 #stores sum of normal loop addition
	parallel_sum = 0 #stores sum of parallel addition

	random_array = [0]*(1500000) #array for the addition

	for i in range(1500000): #assigns random values to the entire array
	        random_array[i]=random.randint(1,10)

	serial_start_time = time.time() #starting time
	serial_sum= arr_sum(random_array,0,1499999,0) #passing parameters to arr_sum function
	serial_elapsed_time = time.time() - serial_start_time #final time taken

	num_cores=multiprocessing.cpu_count() #gives you the number of cores in your computer. you can make loops using the number

	parallel_start_time=time.time() #starting time again

	thread1= Thread(target=arr_sum, args=(random_array,0,187500,0)) #so, thread1 is the variable. thread is the imported function.
	#target should hold the intended function, args has the values to be passed. 
	#i'm passing the array, starting index, ending index and position for the result in parallel_sum_arr
	thread1.start() #starts the running of the thread

	thread2= Thread(target=arr_sum, args=(random_array,187501,375000,1))
	thread2.start()

	thread3= Thread(target=arr_sum, args=(random_array,375001,562500,2))
	thread3.start()
	
	thread4= Thread(target=arr_sum, args=(random_array,562501,750000,3))
	thread4.start()
	
	thread5= Thread(target=arr_sum, args=(random_array,750001,937500,4))
	thread5.start()
	
	thread6= Thread(target=arr_sum, args=(random_array,937501,1125000,5))
	thread6.start()
	
	thread7= Thread(target=arr_sum, args=(random_array,1125001,1312500,6))
	thread7.start()
	
	thread8= Thread(target=arr_sum, args=(random_array,1312501,1499999,7))
	thread8.start()
	
	thread1.join() #closes the thread
	thread2.join()
	thread3.join()
	thread4.join()
	thread5.join()
	thread6.join()
	thread7.join()
	thread8.join()
	for i in range(8): #this adds the values stored by the individual threads together
		parallel_sum=parallel_sum+parallel_sum_arr[i]
	
	parallel_elapsed_time= time.time()-parallel_start_time #final time taken

	print "Serial Time: ", serial_elapsed_time
	print "Parallel Time: ", parallel_elapsed_time

def arr_sum(array,start,end,index): #this function just adds the numbers in the array to sum
	sum=0

	for j in range(start,end):
		sum=sum+array[j]

	parallel_sum_arr[index]=sum #stores the result because you can't return a result from a thread. 
	#hence the need for indexes.

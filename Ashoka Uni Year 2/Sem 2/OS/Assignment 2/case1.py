#Case 1
p=int(input())
n=int(input())

start_message="Sweeny Todd has opened the Barber Shop"
thread_sleep="Sweeny Todd is sleeping"

general_chair=[0]*n

print "Enter 1 for customer, 0 for no customer, and 2 to end customers."

customer_queue=[]
customer_input=0

while (customer_input!=2):
    customer_input=int(input())
    if (customer_input!=2):
        customer_queue.append(customer_input)

print "%s"%start_message

main_chair_status=0
work_timer=0
end_of_customers=0
tick=0
all_done=False
customers_waiting=0
queue_length=len(customer_queue)

while (all_done!=True):
    if (main_chair_status==0):
        if (sum(general_chair)==0):
            if(end_of_customers==1):
                all_done=True
                print "All done!"
            else:
                if (customer_queue[tick]==0):
                    print "%s"%thread_sleep
                else:
                    main_chair_status=customer_queue[tick]
                    work_timer=p
                    print "Customer %s is sitting in the Barber Chair"%main_chair_status
        else:
            main_chair_status=general_chair[0]
            work_timer=p
            print "Customer %s is sitting in the Barber Chair"%main_chair_status

            if(n>1):
                for i in range (n-1):
                    general_chair[i]=general_chair[i+1]
                    general_chair[i+1]=0
            else:
                general_chair[0]=0

            customers_waiting=customers_waiting-1
    else:
        if (customer_queue[tick]!=0):
            if (customers_waiting==n):
                print "The Barbershop is full, customer %s has left"%customer_queue[tick]
            else:
                general_chair[customers_waiting]=customer_queue[tick]
                customers_waiting=customers_waiting+1
        if (work_timer==0):
            print "Customer %s's haircut is complete"%general_chair
            general_chair=0
        else:
            work_timer=work_timer-1
    tick=tick+1

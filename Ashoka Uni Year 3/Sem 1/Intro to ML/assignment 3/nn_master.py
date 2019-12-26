import nn_calcs as nunu
import nn_layer as willump

def get_file_data(file_name):
    x_data=[]
    y_data=[]

    file_read = open(file_name,'r')

    for i in file_read:
        x,y = i.split()

        x_data.append(float(x))
        y_data.append(float(y))

    return x_data,y_data

def part_1_and_2():
    nunu_and_willump=willump.Layer(100)
    nunu_and_willump.initialise()

    training_input,training_output = get_file_data("hw3trainingdata")
    test_input,test_output=get_file_data("hw3testingdata")

    nunu_and_willump.learn(training_input,training_output,0.05,0.01)

    test_error=nunu_and_willump.check(test_input,test_output)

    print ("Test error for part 2: "+str(test_error))

def part_3():
    nunu_and_willump=willump.Layer(200)
    nunu_and_willump.initialise()

    training_input,training_output = get_file_data("hw3trainingdata")
    test_input,test_output=get_file_data("hw3testingdata")

    nunu_and_willump.learn(training_input,training_output,0.05,0.01)

    test_error=nunu_and_willump.check(test_input,test_output)

    print ("Test error for part 3: "+str(test_error))

def part_4():
    nunu_and_willump=willump.Layer(600)
    nunu_and_willump.initialise()

    training_input,training_output = get_file_data("hw3trainingdata")
    test_input,test_output=get_file_data("hw3testingdata")

    nunu_and_willump.learn(training_input,training_output,0.05,0.01)

    test_error=nunu_and_willump.check(test_input,test_output)

    print ("Test error for part 4: "+str(test_error))

def run():
    print ("Starting...")

    part_1_and_2()
    part_3()
    part_4()

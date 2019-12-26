import Tkinter, Tkconstants, tkFileDialog
from Tkinter import *

class Team_Info(object):

    def __init__(self,team_size,winning_prob):
        self.team_size=team_size #number of team members
        self.winning_prob=winning_prob #probability of the team winning

    def MakeMatrix(self,team_size):
        end_matrix=[][]

        print "Select the text file with team member stats \n Make sure the format is height, ',' then weight and separated by line"

        file_dir=Tk()
        file_dir.withdraw()
        file_dir.lift()
        file_dir.title("Select the text file")
        file_dir_name=tkFileDialog.askopenfilename(filetypes=(("Text File","*.txt"),("All Files","*.*")))
        file_dir.destroy()

        data_file=open(file_dir_name,"r")
        process_data=data_file.readlines()
        for x in process_data:
            end_matrix.append(x.split(","))

        crunched_matrix=MatrixCrunch(end_matrix,team_size)

        return crunched_matrix

    def MatrixCrunch(self,matrix,size):
        height_mean=0
        weight_mean=0
        hw_mean_ratio=0

        for i in range(size):
            height_mean=height_mean+matrix[i][0]
            weight_mean=weight_mean+matrix[i][1]
        height_mean=height_mean/size
        weight_mean=weight_mean/size

        hw_mean_ratio=height_mean/weight_mean

        return hw_mean_ratio

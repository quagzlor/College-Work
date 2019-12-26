from os import chdir,getcwd
from math import sin, cos, sqrt, asin, radians
import glob
import pysubs2
import piexif
import csv
from  Tkinter import *
import Tkinter, Tkconstants, tkFileDialog #Used for basic GUI elements
from contextlib import contextmanager

def main():

    print "How many videos do you want to run the program for?"

    valid_entry=False

    while (valid_entry!=True):
        try:
            number_of_vids=input()
            if(number_of_vids>0):
                valid_entry=True
        except:
            print "Please enter it in integer digits"

    number_of_vids_integer=int(number_of_vids)

    for counter_1 in range(number_of_vids_integer):

        print "Please select the folder of images for video %s"%((counter_1+1))

        image_dir = Tk()
        image_dir.withdraw()
        image_dir.lift()
        image_dir.title('Select the image folder')
        image_dir_path = tkFileDialog.askdirectory() #This is used to find the directory which contains the pictures. The GUI used is from Tkinter
        image_dir.destroy()

        chdir(image_dir_path)

        all_image_gps_data=[]

        for filename in glob.iglob('./*.jpg'):
            exif_data_placeholder=exif_data_pull(filename)

            all_image_gps_data.append(exif_data_placeholder)

        print "What distance (in metres) do you want to set for the video?"

        valid_entry=False

        while(valid_entry!=True):

            try:
                video_distance=input()
                if(video_distance>0):
                    valid_entry=True
            except:
                print "Please enter it in integer digits"

        print ("Please select the srt file for the video")

        srt_file_select=Tk()
        srt_file_select.withdraw()
        srt_file_select.lift()
        srt_filename=tkFileDialog.askopenfilename(initialdir = image_dir_path, title = "Select SRT file",filetypes = (("SRT File","*.srt"),("all files","*.*")))
        srt_file_select.destroy()

        srt_data=srt_data_pull(srt_filename)
        srt_full_data=distance_compare(srt_data,all_image_gps_data,video_distance)
        write_to_csv(zip(*srt_full_data),"Images at Video Timings",counter_1)

        print "What distance (in metres) do you want to set for the points of interest?"

        valid_entry=False

        while(valid_entry!=True):

            try:
                poi_distance=input()
                if(poi_distance>0):
                    valid_entry=True
            except:
                print "Please enter it in integer digits"

        print ("Please select the csv file for the points of interest")

        csv_file_select=Tk()
        csv_file_select.withdraw()
        csv_file_select.lift()
        csv_filename=tkFileDialog.askopenfilename(initialdir = image_dir_path, title = "Select CSV file",filetypes = (("Comma Separated Values","*.csv"),("all files","*.*")))
        csv_file_select.destroy()

        csv_data=csv_data_pull(csv_filename)
        csv_full_data=distance_compare(csv_data,all_image_gps_data,poi_distance)
        write_to_csv(zip(*csv_full_data),"Images near Points of Interest",counter_1)
                
def exif_data_pull(image_name):

    exif_dict = piexif.load(image_name)

    gps_data_dump = exif_dict.pop("GPS")

    try:
        latitude=[gps_data_dump[2][0],gps_data_dump[2][1],gps_data_dump[2][2]]

        longitude=[gps_data_dump[4][0],gps_data_dump[4][1],gps_data_dump[4][2]]

        gps_data=[]

        gps_data.append(float(latitude[0][0]))
        gps_data.append(float(latitude[1][0]))
        gps_data.append(float(latitude[2][0]))

        gps_data.append(float(longitude[0][0]))
        gps_data.append(float(longitude[1][0]))
        gps_data.append(float(longitude[2][0]))

        gps_data_true=dms_to_dd(gps_data[0],gps_data[1],gps_data[2],gps_data[3],gps_data[4],gps_data[5])
    except:
        print ("End of files")
        gps_data_true=0

    if (gps_data_true==0):
        return []

    return image_name,gps_data_true[0],gps_data_true[1]

def dms_to_dd(deg_1,min_1,sec_1,deg_2,min_2,sec_2):

    placeholder_1=float(min_1+(sec_1/60))
    placeholder_1=float(deg_1+(placeholder_1/60))

    placeholder_2=float(min_2+(sec_2/60))
    placeholder_2=float(deg_2+(placeholder_2/60))

    return placeholder_1,placeholder_2

def get_gps_distance(latitude_1,longitude_1,latitude_2,longitude_2):
    approx_earth_radius = 6372.8

    lat_1=float(radians(latitude_1))
    lat_2=float(radians(latitude_2))
    difference_latitude =float(radians(latitude_2-latitude_1))
    difference_longitude =float(radians(longitude_2-longitude_1))

    placeholder_1 =float(sin(difference_latitude / 2)**2 + cos(lat_1) * cos(lat_2) * sin(difference_longitude / 2)**2)
    placeholder_2 =float(2*asin(sqrt(placeholder_1)))

    gps_distance=approx_earth_radius*placeholder_2

    return gps_distance

def is_within_distance(main_gps,list_gps,distance_to_check):

    within_range=[]
    
    for counter_1 in range((len(list_gps[0][0]))):
        found_gps_distance=(get_gps_distance(main_gps[0],main_gps[1],list_gps[counter_1][1],list_gps[counter_1][2])/1000)

        if(found_gps_distance<distance_to_check):
            
            within_range.append(str(list_gps[counter_1][0]))
            within_range.append("|")
            
    return within_range

def srt_data_pull(srt_file):
    subs_file=pysubs2.load(srt_file)
    ordered_subs_lat=[]
    ordered_subs_long=[]
    ordered_subs_time=[]

    for line in subs_file:
        ordered_subs_time.append((int(line.start))/1000)
        text_placeholder=(line.text).split(',')
        ordered_subs_lat.append(float(text_placeholder[0]))
        ordered_subs_long.append(float(text_placeholder[1]))

    ordered_subs_final=[ordered_subs_time,ordered_subs_lat,ordered_subs_long]

    return ordered_subs_final

def write_to_csv(data_to_write,title,serial_number):

    title=title+str(serial_number)

    csv_file=open('%s.csv'%title,'w')
    with csv_file:
        writer=csv.writer(csv_file,dialect='excel')
        writer.writerows(data_to_write)
    csv_file.close()

    current_dir=getcwd()
    
    print "File saved at %s"%current_dir

def distance_compare(data_list_1,data_list_2,distance):
    location_list=[]
    image_list=[]

    for counter_1 in range(len(data_list_1[0])):
        location_data_holder=[data_list_1[1][counter_1],data_list_1[2][counter_1]]
        image_holder=is_within_distance(location_data_holder,data_list_2,distance)

        location_list.append(data_list_1[0][counter_1])
        image_list.append(str(image_holder))
    final_data=[location_list,image_list]

    return final_data

def csv_data_pull(csv_file):

    location_list=[]
    lat_list=[]
    long_list=[]

    with open(csv_file) as file_to_read:
        reader = csv.DictReader(file_to_read)
        for row in reader:
            location_list.append(row['asset_name'])
            lat_list.append(float(row['latitude']))
            long_list.append(float(row['longitude']))
            
    full_csv_data= [location_list,lat_list,long_list]

    return full_csv_data
            
main()

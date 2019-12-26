#v0.1 of Ashoka Autologin
#This project is covered under GNU GPLv3 licence
import time
import os
import os.path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

login_page="http://10.1.0.100:8090/"
password=""
time_delay=""
test_page="https://www.google.com"

if os.path.isfile("Autologin_Data.txt")!=True:
    print "What is the username?"
    username=raw_input()
    print "What is the password?"
    password=raw_input()
    print "After how many hours do you want to log in again?"
    time_delay=raw_input()


    save_file= open("Autologin_Data.txt","w")
    save_file.write(username)
    save_file.write('\n')
    save_file.write(password)
    save_file.write('\n')
    save_file.write(time_delay)
    save_file.close()

save_file=open("Autologin_Data.txt","r")
login_username=save_file.readline()
login_password=save_file.readline()
time_delay=int(save_file.readline())
save_file.close()

while 1==1:
    try:
        browser = webdriver.Edge("C:\\Ashoka Autolog\MicrosoftWebDriver.exe")
        browser.get(login_page)

        main_window_handle = browser.current_window_handle

        send_username = browser.find_element_by_name("username").send_keys(login_username)

        alert = browser.switch_to_alert()
        alert.accept()

        browser.switch_to.window(main_window_handle)
        send_userpass = browser.find_element_by_name("password").send_keys(login_password)

        browser.find_element_by_name("btnSubmit").click()
    except :
        pass

    time.sleep(10)

    os.system('taskkill /f /im MicrosoftWebDriver.exe')
    os.system('taskkill /f /im MicrosoftEdge.exe')

    time.sleep(60*60*time_delay)

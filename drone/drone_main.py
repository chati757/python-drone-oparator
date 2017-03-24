#!/usr/bin/env python
#-*-coding: utf-8 -*-
import threading
import socket #client side
import time

from drone_init import *

#register stage get from database and GPIO setting

def main():
    global lockthread
    print("in main")
#------------------main thread worker--------------------- 

#check connection before start 
    #if cannot connect ,run connection()
connection()
#socket update routine from c&c server or http server (request tcp and receive json format)

#get mode_info from database
#if[mode 2]
    #drone is online [greenlight to station]
    #(listening)wait station response [station request initialize_data]
        #(response)mode_info (full or semi)
        #(response)send to display current routine from drone side

        #(listening)choice > auto_pilot()[global value =0] or manual_control()[global value =1]
        #(response)commit choice
        #(listening)socket wait command from c&c server to start command or option command
            #if option command (change choice again or change mode)
                #id change choice
                    #choice = new choice 
                #if change mode
                    #update mode_info 
            #continue line 29 again > (listening)socket wait command from c&c server to start command or option command
            #if start command
                #(response)started..
                    #separate and run thread from choice
                
#if[mode 1] 
    #pass
    #default separate thread run auto_pilot [global value =0]

#loop running = true (listening command)
    #option > stop drone command [global value =-1 kil all daemon thread] 
    #option > update routine
         #> stop drone command [global value =-1 kil all daemon thread]
         #> update_routine()
    #option > switching auto_pilot , man_control [with global value (0,1)]
        #check number thread must have 1 only
        #separate and run thread from choice again


#-------------------main thread function--------------------
def connection():
    global CON_COUNT
    try:
        s = socket.socket()
        s.connect((HOST_S,POST_S))
        CON_COUNT = 0
        message = "empty"
        while message != '':
            data = s.recv(3072)
            print('station response : '+data_res)
            message = raw_input("->")
            s.send(message)
        s.close
    except IOError as e:
        if(e.errno==10061):
            print("cannot connect , trying..["+CON_COUNT+"]")
            reconnection()
        else
            print(e)

def reconnection():
    #reconnection 5 time if more then 
    #if thread separated or thread more then 1 run reconnection again every 10 seconds
    #else os.exit() and wait for ssh and reboot again
    if(threading.active_count()>1 or CON_COUNT<=5):
        CON_COUNT+=1
        connection()
    else
        print("connection is lost , wait for reboot form user.")
        os.exit()
        
#abount database 
def update_routine():
    print("in update_routine")

#drone_routine.py
def get_routine():
    print("in get_routine")
    #drone_routine.py
#-------------------daemon thread function--------------------
def auto_pilot():
    global mode,lockthread
    lockthread.acquire()
    try:
        while(mode==0):
            print("in auto_pilot")
            time.sleep(1)
            pass
        manual_control()
    finally:
        lockthread.release()
    #loop if global value =1 break and kill thread this loop and go man_control
    #get routine

def manual_control():
    global mode,lockthread
    lockthread.acquire()
    try:
        while(mode==1):
            print("in man_control")
            time.sleep(1)
            pass
        auto_pilot()
    finally:
        lockthread.release()
    #loop if global value =0 break and kill thread this loop and go auto_pilot

def check_connection():
    print("check_connection")
    #ping server and check server response


if(__name__=="__main__"):
    #main()
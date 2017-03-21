#!/usr/bin/env python
#-*-coding: utf-8 -*-
import threading
import socket #client side

register():
#register stage get from database and GPIO setting

main():
#------------------main thread worker---------------------
# 2 mode [store in mode_info database]
# 1.full-automation mode (start routine by itself) 
# 2.semi-automation mode (start routine by myself) 

#check connection before start 
    #if cannot connect run reconnection()

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
reconnection():
#reconnection 5 time if more then 
    #if thread separated or thread more then 1 run reconnection again
    #else os.exit() and wait for ssh and reboot again

#abount database 
update_routine():
#drone_routine.py
get_routine():
#drone_routine.py
#-------------------daemon thread function--------------------
auto_pilot():
#loop if global value =1 break and kill thread this loop and go man_control
#get routine

manual_control():
#loop if global value =0 break and kill thread this loop and go auto_pilot

check_connection():
#ping server and check server response

if(__name__=="__main__"):
    main()
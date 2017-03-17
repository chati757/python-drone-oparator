#!/usr/bin/env python
#-*-coding: utf-8 -*-
from unicurses import *
from station_init import *
from station_position import *
from station_info import *
from station_console import *
from station_loadout import *
from station_detail import *

#-----------------main panel----------------
MAIN_STATION_MARGIN_TOP=1


def main():
    #-------------draft window------------------
    #draftwin(stdscr)
    #center(79 25) all(158 50) work space (154 44)
    #-------------------------------------------
    #-----------create main station-------------
    create_main_station()
    #-----------create position panel-----------
    create_main_position_panel()
    create_sub_position_panel("01","T01","NAME01",DRONE_IMAGE_1,("xxx"+" %"),"MAINTENANCE","OFFLINE",0)
    create_sub_position_panel("02","T02","NAME02","EMPTY",("xxx"+" %"),"MAINTENANCE","OFFLINE",20)
    create_sub_position_panel("03","T03","NAME03","EMPTY",("xxx"+" %"),"MAINTENANCE","OFFLINE",40)
    create_sub_position_panel("04","T04","NAME04","EMPTY",("xxx"+" %"),"MAINTENANCE","OFFLINE",60)
    #-----------create station information-------
    create_main_information_panel()
    #-----------create station console-----------
    create_main_console_panel()
    #-----------create station loadout-----------
    create_main_loadout_panel()
    #-----------create station detail------------
    create_main_detail_panel()
    
    
    running = True
    while(running):
        key=getch()#don't forget setting window2 or window in this line
        if(key==27):
            running = False
            break

    endwin() #for stop ncurses

    return 0

def draftwin(stdscr):
    global MAX_Y
    global MAX_X
    move(MAX_Y/2,MAX_X/2)
    addstr("[ @ ]"+"center x= "+str(MAX_X/2)+" center y= "+str(MAX_Y/2))
    move((MAX_Y/2)+1,(MAX_X/2))
    addstr("[max colums x= "+str(MAX_X)+" max rows y= "+str(MAX_Y)+"]")

def create_main_station():
    global MAIN_STATION_MARGIN_TOP
    global MAX_Y
    global MAX_X
    window_main_sta=newwin(MAX_Y-2,MAX_X,0,0)
    box(window_main_sta)

    window_main_logo=newwin(3,11,0,0)
    box(window_main_logo)
    wmove(window_main_logo,1,1)
    waddstr(window_main_logo," STATION ")

    w_panel=new_panel(window_main_sta)
    move_panel(w_panel,MAIN_STATION_MARGIN_TOP,0)
    logo_panel=new_panel(window_main_logo)
    move_panel(logo_panel,0,MAX_X/4)

if(__name__=="__main__"):
    main()
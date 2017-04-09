#!/usr/bin/env python
#-*-coding: utf-8 -*-
import threading
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
    #every creation have endwin except create_main_information_panel
    #-------------draft window------------------
    #draftwin(stdscr)
    #center(79 25) all(158 50) work space (154 44)
    #-------------------------------------------
    #-----------create main station-------------
    create_main_station()
    #-----------create position panel-----------
    #create_mainsub_position_panel()
    #thread sub position panel
    th_mspos=threading.Thread(target=create_mainsub_position_panel,name="thread mainsub position")
    #-----------create station information-------
    #thread info
    th_info=threading.Thread(target=create_main_information_panel,name="thread info")
    #-----------create station loadout-----------
    create_main_loadout_panel()
    #-----------create station detail------------
    create_main_detail_panel()
    #-----------create station console-----------
    #thread console
    th_console=threading.Thread(target=create_main_console_panel,name="thread console")

    #-----------initialize thread---------------
    th_mspos.setDaemon(True)
    th_mspos.start()
    th_info.setDaemon(True)
    th_info.start()
    th_console.start()

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
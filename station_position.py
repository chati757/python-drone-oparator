#!/usr/bin/env python
#-*-coding: utf-8 -*-
from unicurses import * 
from make_color import *
#declare for testing station_position.py
from station_init import *

def main():
    #-------------draft window------------------
    #draftwin(stdscr)
    #center(79 25) all(158 50) work space (154 44)
    #-------------------------------------------
    #-----------create position panel-----------
    create_main_position_panel()
    create_sub_position_panel("01","T01","NAME01",("xxx"+" %"),"MAINTENANCE","OFFLINE",0)
    create_sub_position_panel("02","T02","NAME02",("xxx"+" %"),"MAINTENANCE","OFFLINE",20)
    create_sub_position_panel("03","T03","NAME03",("xxx"+" %"),"MAINTENANCE","OFFLINE",40)
    create_sub_position_panel("04","T04","NAME04",("xxx"+" %"),"MAINTENANCE","OFFLINE",60)

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

def create_main_position_panel():
    global POSITION_PANEL_SIZE_HIGH
    global POSITION_PANEL_SIZE_WIDTH
    global POSITION_PANEL_POS_Y
    global POSITION_PANEL_POS_X
    #-------------station main slot panel-----------
    #total size width 80 high 22
    window_main_pos=newwin(POSITION_PANEL_SIZE_HIGH,POSITION_PANEL_SIZE_WIDTH,0,0)
    box(window_main_pos)
    wmove(window_main_pos,0,35)
    waddstr(window_main_pos," POSITION ")
    ws_panel=new_panel(window_main_pos)
    move_panel(ws_panel,POSITION_MARGIN_TOP,POSITION_PANEL_POS_X)

def create_sub_position_panel(num_data,id_data,name_data,batt_data,status_data,conn_data,pos):
    global POSITION_PANEL_SIZE_HIGH
    global POSITION_PANEL_SIZE_WIDTH
    global POSITION_PANEL_POS_Y
    global POSITION_PANEL_POS_X
    global MAX_Y
    global MAX_X

    #-------------station slot node------------
    #total width 20  high 22
    #add condition not less 20 and 22

    window_sub_slot=newwin(20,20,0,0)
    box(window_sub_slot)
    wmove(window_sub_slot,1,2)
    waddstr(window_sub_slot,"ID:"+id_data)
    wmove(window_sub_slot,2,1)
    whline(window_sub_slot,ACS_HLINE,18)
    wmove(window_sub_slot,1,14)
    wvline(window_sub_slot,ACS_VLINE,1)
    wmove(window_sub_slot,1,16)
    waddstr(window_sub_slot,num_data)
    wmove(window_sub_slot,3,2)
    waddstr(window_sub_slot,"NAME:"+name_data)
    wmove(window_sub_slot,4,1)
    whline(window_sub_slot,ACS_HLINE,18)
    wmove(window_sub_slot,13,1)
    whline(window_sub_slot,ACS_HLINE,18)
    wmove(window_sub_slot,14,2)
    waddstr(window_sub_slot,"BATT. "+batt_data)
    wmove(window_sub_slot,15,1)
    whline(window_sub_slot,ACS_HLINE,18)
    wmove(window_sub_slot,16,2)

    waddstr(window_sub_slot,status_data)
    wmove(window_sub_slot,16,16)
    if (status_data=="READY"):
        waddstr(window_sub_slot,"  ",color_pair(GREENLIGHT))
    elif ((status_data=="MAINTENANCE") or (status_data=="NOT READY")):
        waddstr(window_sub_slot,"  ",color_pair(REDLIGHT))
    else:
        waddstr(window_sub_slot,"ERR")

    wmove(window_sub_slot,17,1)
    whline(window_sub_slot,ACS_HLINE,18)

    wmove(window_sub_slot,18,2)
    waddstr(window_sub_slot,conn_data)
    wmove(window_sub_slot,18,16)
    if (conn_data=="ONLINE"):
        waddstr(window_sub_slot,"  ",color_pair(GREENLIGHT))
    elif (conn_data=="OFFLINE"):
        waddstr(window_sub_slot,"  ",color_pair(REDLIGHT))
    else:
        waddstr(window_sub_slot,"ERR")
        

    #window_sub_slot_2=newwin(21,20,0,0)
    #box(window_sub_slot_2)
    
    #-------------all panel component----------
    wss_panel=new_panel(window_sub_slot)

    #wss_panel_2=new_panel(window_sub_slot_2)

    #-------------manage panel position--------
    move_panel(wss_panel,POSITION_MARGIN_TOP+1,POSITION_PANEL_POS_X+pos)

    #move_panel(wss_panel_2,1,20)
    #int border(chtype ls, chtype rs, chtype ts, chtype bs, chtype tl, chtype tr, chtype bl, chtype br)

    #-------------panel update stage-----------
    update_panels()
    doupdate()
    
def make_color(fg,bg):
    global MAKE_COLOR_NUM

    color_number = MAKE_COLOR_NUM
    init_pair(color_number,fg,bg)
    MAKE_COLOR_NUM +=1
    
    return MAKE_COLOR_NUM

if(__name__=="__main__"):
    main()
#!/usr/bin/env python
#-*-coding: utf-8 -*-
from unicurses import * 
from make_color import *
#declare for testing station_position.py
from station_init import *

def main():
    
    create_main_detail_panel()
    

    running = True
    while(running):
        key=getch()#don't forget setting window2 or window in this line
        if(key==27):
            running = False
            break

    endwin() #for stop ncurses

    return 0

def create_main_detail_panel():
    #-------------station main slot panel-----------
    #total size width 80 high 22
    window_main_detail=newwin(DETAIL_PANEL_SIZE_HIGH,DETAIL_PANEL_SIZE_WIDTH,0,0)
    box(window_main_detail)
    wmove(window_main_detail,0,16)
    waddstr(window_main_detail," DETAIL ",A_REVERSE)
    ws_panel=new_panel(window_main_detail)
    move_panel(ws_panel,DETAIL_MARGIN_TOP,DETAIL_PANEL_POS_X)
    update_panels()
    doupdate()

if(__name__=="__main__"):
    main()
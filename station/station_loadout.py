#!/usr/bin/env python
#-*-coding: utf-8 -*-
from unicurses import * 
from make_color import *
#declare for testing station_position.py
from station_init import *

def main():
    
    create_main_loadout_panel()
    

    running = True
    while(running):
        key=getch()#don't forget setting window2 or window in this line
        if(key==27):
            running = False
            break

    endwin() #for stop ncurses

    return 0

def create_main_loadout_panel():
    #-------------station main slot panel-----------
    #total size width 80 high 22
    window_main_loadout=newwin(LOADOUT_PANEL_SIZE_HIGH,LOADOUT_PANEL_SIZE_WIDTH,0,0)
    box(window_main_loadout)
    wmove(window_main_loadout,0,16)
    waddstr(window_main_loadout," LOADOUT ",A_REVERSE)
    wmove(window_main_loadout,((LOADOUT_PANEL_SIZE_HIGH/2)-1),1)
    whline(window_main_loadout,ACS_HLINE,38)

    ws_panel=new_panel(window_main_loadout)
    move_panel(ws_panel,LOADOUT_MARGIN_TOP,LOADOUT_PANEL_POS_X)
    update_panels()
    doupdate()

if(__name__=="__main__"):
    main()
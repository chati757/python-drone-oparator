#!/usr/bin/env python
#-*-coding: utf-8 -*-
import time
from unicurses import * 
from make_color import *
#declare for testing station_position.py
from station_init import *

content_line = []

def main():
    create_main_information_panel()
    

def create_main_information_panel():
    #-------------station main slot panel-----------
    #total size width 80 high 22
    window_main_info=newwin(INFORMATION_PANEL_SIZE_HIGH,INFORMATION_PANEL_SIZE_WIDTH,0,0)
    #box(window_main_info)
    showbox(window_main_info," INFORMATION ",5)
    ws_panel=new_panel(window_main_info)
    move_panel(ws_panel,INFORMATION_MARGIN_TOP,INFORMATION_PANEL_POS_X)
    
    running = True
    for i in range(20):
        addstring(window_main_info,"testing:"+str(i))
        time.sleep(1)
    
    endwin() #for stop ncurses
    
def showbox(window,txt,shiftcenter):
    box(window)
    wmove(window,0,shiftcenter)
    waddstr(window,txt,A_REVERSE)

def addstring(window,string):
    global INFORMATION_COUNT_LINE
    global content_line
    buffer=0
    #INFORMATION_PANEL_SIZE_HIGH-2 is max row content in box
    if (INFORMATION_COUNT_LINE > INFORMATION_PANEL_SIZE_HIGH-2):
        wclear(window)
        showbox(window," INFORMATION ",5)
        buffer = INFORMATION_COUNT_LINE
        INFORMATION_COUNT_LINE = 2 # row position 2 is first content in box
        for i in range(len(content_line)):
            if(i<len(content_line)-1):
                content_line[i]=content_line[i+1]
            else:
                content_line[i]=string
            #debug loop mode
            #mvwaddstr(window,INFORMATION_COUNT_LINE+i,INFORMATION_INNER_INFO_COL,(str(i),len(content_line)))
            mvwaddstr(window,INFORMATION_COUNT_LINE+i,INFORMATION_INNER_INFO_COL,content_line[i])
            update_panels()
            doupdate()
        INFORMATION_COUNT_LINE=buffer
        '''
        INFORMATION_COUNT_LINE = 2 # row position 2 is first content in box
        wclear(window)
        showbox(window," INFORMATION ",5)
        ''' 
    else:
        content_line.append(string)
        mvwaddstr(window,INFORMATION_COUNT_LINE,INFORMATION_INNER_INFO_COL,string)
        INFORMATION_COUNT_LINE=INFORMATION_COUNT_LINE+1
        update_panels()
        doupdate()

if(__name__=="__main__"):
    main()
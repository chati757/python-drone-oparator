#!/usr/bin/env python
#-*-coding: utf-8 -*-
from unicurses import * 
from make_color import *
#declare for testing station_position.py
from station_init import *

def main():
    
    create_main_console_panel()
    
def create_main_console_panel():
    global CONSOLE_COUNT_LINE
    #-------------station main slot panel-----------
    #total size width 80 high 22
    window_main_console=newwin(CONSOLE_PANEL_SIZE_HIGH,CONSOLE_PANEL_SIZE_WIDTH,0,0)
    showbox(window_main_console," CONSOLE ",5)
    ws_panel=new_panel(window_main_console)
    move_panel(ws_panel,CONSOLE_MARGIN_TOP,CONSOLE_PANEL_POS_X)
    
    running = True
    while(running):
        if (wgetch(window_main_console)!=""):
            echo()
            curs_set(True)
        choice = curses_raw_input(window_main_console,CONSOLE_INNER_CMD_ROW,CONSOLE_INNER_CMD_COL, "command : ").lower()
        if (choice!=""):
           #mvwaddstr(window,2,3,"in clear")
            CONSOLE_COUNT_LINE=CONSOLE_INNER_INFO_ROW #reset line inner info
            wclear(window_main_console)

        if (choice == "man" or choice == "manual" or choice == "help"):
            addstring(window_main_console,"[MAIN] command :")
            addstring(window_main_console,"")
            addstring(window_main_console," man [manual] - show manual")
            addstring(window_main_console," ver [version] - show version")
            addstring(window_main_console," exit - close program")
            addstring(window_main_console,"")
            addstring(window_main_console,"[DRONE] command :")
            addstring(window_main_console,"")
            addstring(window_main_console," DRONE REGISTER :")
            addstring(window_main_console," dr reg new <new drone id> - create data drone for station")
            addstring(window_main_console," dr reg edit <drone id> - edit drone database")
            addstring(window_main_console," dr reg del <drone id> - remove drone form database")
            addstring(window_main_console,"")
            addstring(window_main_console,"[SERVER CONNECTION] command :")
            addstring(window_main_console,"")
            addstring(window_main_console,"[LOADOUT] command :")

        elif (choice == "ver" or choice == "version"):
            addstring(window_main_console,"PYDROBOT VERSION : ALPHA")

        elif (choice == "exit"):
            showbox(window_main_console," CONSOLE ",5)
            break
        else:
            mvwaddstr(window_main_console,CONSOLE_INNER_INFO_ROW,CONSOLE_INNER_INFO_COL,"Invalid Command - unknow syntax")

        showbox(window_main_console," CONSOLE ",5)
    update_panels()
    doupdate()
    endwin() #for stop ncurses

def showbox(window,txt,shift):
    box(window)
    wmove(window,0,shift)
    waddstr(window,txt,A_REVERSE)

def addstring(window,string):
    global CONSOLE_COUNT_LINE
    #CONSOLE_PANEL_SIZE_HIGH-2 is max row content in box
    #if content overflow back to first line
    if(CONSOLE_COUNT_LINE>CONSOLE_PANEL_SIZE_HIGH-2):
        CONSOLE_COUNT_LINE=2 # row position 2 is first content in box
        wclear(window)
        showbox(window," CONSOLE ",5)
    mvwaddstr(window,CONSOLE_COUNT_LINE,CONSOLE_INNER_INFO_COL,string)
    CONSOLE_COUNT_LINE=CONSOLE_COUNT_LINE+1

def curses_raw_input(window,row,col, prompt_string):
    #display cool or hot?
    mvwaddstr(window,row,col,prompt_string) #mvaddstr(r, c, prompt_string)
    #refresh() #return to line 1 again
    input = mvwgetstr(window,(row),col+10) #wait input for this line
    return input

if(__name__=="__main__"):
    main()
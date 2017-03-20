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
    window_main_info=newwin(CONSOLE_PANEL_SIZE_HIGH,CONSOLE_PANEL_SIZE_WIDTH,0,0)
    showbox(window_main_info," CONSOLE ",5)
    ws_panel=new_panel(window_main_info)
    move_panel(ws_panel,CONSOLE_MARGIN_TOP,CONSOLE_PANEL_POS_X)

    running = True
    while(running):
        choice = curses_raw_input(window_main_info,CONSOLE_INNER_CMD_ROW,CONSOLE_INNER_CMD_COL, "command : ").lower()
        if (choice!=""):
           #mvwaddstr(window,2,3,"in clear")
            CONSOLE_COUNT_LINE=CONSOLE_INNER_INFO_ROW #reset inner info
            wclear(window_main_info)

        if (choice == "man" or choice == "manual" or choice == "help"):
            addstring(window_main_info,"[MAIN] command :")
            addstring(window_main_info,"")
            addstring(window_main_info,"man [manual] - show manual")
            addstring(window_main_info,"ver [version] - show version")
            addstring(window_main_info,"exit - close program")
            addstring(window_main_info,"")
            addstring(window_main_info,"[CONNECTION] command :")
            addstring(window_main_info,"")
            addstring(window_main_info,"[LOADOUT] command :")

        elif (choice == "ver" or choice == "version"):
            addstring(window_main_info,"PYDROBOT VERSION : BETA")

        elif (choice == "exit"):
            showbox(window_main_info," CONSOLE ",5)
            break
        else:

            mvwaddstr(window_main_info,CONSOLE_INNER_INFO_ROW,CONSOLE_INNER_INFO_COL,"Invalid Command - unknow syntax")

        showbox(window_main_info," CONSOLE ",5)
    update_panels()
    doupdate()
    endwin() #for stop ncurses

def showbox(window,txt,shift):
    box(window)
    wmove(window,0,shift)
    waddstr(window,txt,A_REVERSE)

def addstring(window,string):
    global CONSOLE_COUNT_LINE
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
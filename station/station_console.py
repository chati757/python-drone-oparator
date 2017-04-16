#!/usr/bin/env python
#-*-coding: utf-8 -*-
from unicurses import * 
from make_color import *
#declare for testing station_position.py
from station_init import *
from station_database import *

def main():
    
    create_main_console_panel()
    
def create_main_console_panel():
    global CONSOLE_COUNT_LINE
    echo()
    curs_set(True)
    #-------------station main slot panel-----------
    #total size width 80 high 22
    window_main_console=newwin(CONSOLE_PANEL_SIZE_HIGH,CONSOLE_PANEL_SIZE_WIDTH,0,0)
    showbox(window_main_console," CONSOLE ",5)
    ws_panel=new_panel(window_main_console)
    move_panel(ws_panel,CONSOLE_MARGIN_TOP,CONSOLE_PANEL_POS_X)
    
    running = True
    while(running):
        choice = curses_raw_input(window_main_console, "command : ").lower()

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
            addstring(window_main_console,"[DRONE REGISTER] command :")
            addstring(window_main_console," dr reg new - add new drone data form database")
            addstring(window_main_console," dr reg edit - edit drone data form database")
            addstring(window_main_console," dr reg del - delete drone data form database")
            addstring(window_main_console,"")
            addstring(window_main_console,"[SERVER CONNECTION] command :")
            addstring(window_main_console,"")
            addstring(window_main_console,"[LOADOUT] command :")
        
        elif (choice == "dr reg new" or choice == "drone register new"):
            addstring(window_main_console,"entering to add new drone stage")
            addstring(window_main_console,"")
            addstring(window_main_console,"---current drone database---")
            addstring(window_main_console,"")
            #show current drone id
            fetch_alldrone(window_main_console)
            addstring(window_main_console,"")
            addstring(window_main_console,"[i] for insert new data and [ENTER] for confirm")
            addstring(window_main_console,"[ESC] for exit ")
            
            running2 = True
            while running2:
                reset_origin_curser(window_main_console,"command : ")
                presskey=wgetch(window_main_console)

                if(presskey==105):
                    addstring(window_main_console,"--insert mode--")

                    drone_id = curses_raw_input(window_main_console,"name id : ").lower()
                    drone_name = curses_raw_input(window_main_console,"name drone : ").lower()
                    drone_pos_slot = curses_raw_input(window_main_console,"position slot : ").lower()
                    drone_detail=curses_raw_input(window_main_console,"drone detail : ").lower()
                    
                    addstring(window_main_console,"you need to save this dataset ? Y/N") 
                    
                    running3 = True
                    while running3:
                        reset_origin_curser(window_main_console,"command : ")
                        presskey=wgetch(window_main_console)

                        if(presskey==121): #[y]
                            addstring(window_main_console,"saving data..")
                            addstring(window_main_console,"saved data")
                            running3 = False
                        elif(presskey==110): #[n]
                            addstring(window_main_console,"cancel data")
                            running3 = False
                        else:
                            addstring(window_main_console,"incorect key !")


                elif(presskey==27):
                    addstring(window_main_console,"--exit insert mode--")
                    running2 = False

                else:
                    addstring(window_main_console,"incorect key !")
            #check key not ESC
                #input new drone id 
                    #check not duplicate data id
            

        elif (choice == "dr reg edit" or choice == "drone register edit"):
            addstring(window_main_console,"entering to drone editor stage")
            addstring(window_main_console,"")
            addstring(window_main_console,"---current drone database---")
            addstring(window_main_console,"")
            #show current drone id
            fetch_alldrone(window_main_console)
            #input new drone id 
            #receive console command

        elif (choice == "dr reg del" or choice == "drone register delete"):
            addstring(window_main_console,"entering to delete drone stage")
            addstring(window_main_console,"")
            addstring(window_main_console,"---current drone database---")
            addstring(window_main_console,"")
            #show current drone id
            fetch_alldrone(window_main_console)
            #input new drone id 
            #receive console command

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

def reset_origin_curser(window,prefix=""):
    global CONSOLE_INNER_CMD_ROW,CONSOLE_INNER_CMD_COL,CONSOLE_PANEL_SIZE_WIDTH
    showbox(window," CONSOLE ",5)
    mvwaddstr(window,CONSOLE_INNER_CMD_ROW,CONSOLE_INNER_CMD_COL,(" "*(CONSOLE_PANEL_SIZE_WIDTH-4)))#refresh prefix string
    mvwaddstr(window,CONSOLE_INNER_CMD_ROW,CONSOLE_INNER_CMD_COL,prefix)# origin curser
    

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

def curses_raw_input(window,prompt_string):
    global CONSOLE_PANEL_SIZE_WIDTH,CONSOLE_INNER_CMD_ROW,CONSOLE_INNER_CMD_COL
    #display cool or hot?
    reset_origin_curser(window)
    mvwaddstr(window,CONSOLE_INNER_CMD_ROW,CONSOLE_INNER_CMD_COL,(" "*(CONSOLE_PANEL_SIZE_WIDTH-4)))#refresh prefix string
    mvwaddstr(window,CONSOLE_INNER_CMD_ROW,CONSOLE_INNER_CMD_COL,prompt_string) #mvaddstr(r, c,prompt_string)
    #refresh() #return to line 1 again
    input = mvwgetstr(window,CONSOLE_INNER_CMD_ROW,CONSOLE_INNER_CMD_COL+len(prompt_string)) #wait input for this line
    return input

def fetch_alldrone(window):
    global redis
    alldrone=redis.keys("drone:**:main")
    #addstring(window,alldrone)
    for i in range(len(alldrone)):
        addstring(window,alldrone[i])


if(__name__=="__main__"):
    main()
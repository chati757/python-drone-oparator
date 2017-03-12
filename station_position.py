from unicurses import * 

#-----------------------------------------initalize stage----------------------------------------------
stdscr = initscr() #start up screen and initalize ncurses
#-----------determate default window---------------
start_color()#default is white
noecho()#not show txt when typing
curs_set(False)#not show cursor
keypad(stdscr,True)#register arrow key 

#-------------draft window------------------
#draftwin(stdscr)
#center(79 25) all(158 50) work space (154 44)
#-------------------------------------------

#-----------------layout--------------------
MAX_Y,MAX_X=getmaxyx(stdscr)

#----------position panel layout------------
#size high 22 width 80 
#position x = 154-(154-80) = 74
#position y = 44/2 = 22
POSITION_PANEL_Y=22
POSITION_PANEL_X=74

def main():
    #-----------create position panel-----------
    create_position_panel()

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

def create_position_panel():
    global POSITION_PANEL_Y
    global POSITION_PANEL_X
    global MAX_Y
    global MAX_X
    #-------------station slot panel-----------
    #total width 80 high 22
    window_slot=newwin(22,80,0,0)
    box(window_slot)
    wmove(window_slot,0,35)
    waddstr(window_slot," POSITION ")

    #-------------station slot node------------
    #total width 20  high 22
    #add condition not less 20 and 22

    window_sub_slot_1=newwin(20,20,0,0)
    box(window_sub_slot_1)
    wmove(window_sub_slot_1,1,2)
    waddstr(window_sub_slot_1,"ID: ")
    wmove(window_sub_slot_1,1,16)
    waddstr(window_sub_slot_1,"xx")
    wmove(window_sub_slot_1,3,2)
    waddstr(window_sub_slot_1,"NAME: ")
    wmove(window_sub_slot_1,14,2)
    waddstr(window_sub_slot_1,"batt. ")
    wmove(window_sub_slot_1,16,2)
    waddstr(window_sub_slot_1,"xxxx")
    wmove(window_sub_slot_1,18,2)
    waddstr(window_sub_slot_1,"xxxx")

    #window_sub_slot_2=newwin(21,20,0,0)
    #box(window_sub_slot_2)
    
    #-------------all panel component----------
    ws_panel=new_panel(window_slot)
    wss_panel_1=new_panel(window_sub_slot_1)

    #wss_panel_2=new_panel(window_sub_slot_2)

    #-------------manage panel position--------
    move_panel(wss_panel_1,1,0)

    #move_panel(wss_panel_2,1,20)

    #-------------panel update stage-----------
    update_panels()
    doupdate()
    #-------------separate panel line----------
    move(3,1)
    hline(ACS_HLINE,18)
    move(2,14)
    vline(ACS_VLINE,1)
    move(5,1)
    hline(ACS_HLINE,18)
    move(14,1)
    hline(ACS_HLINE,18)
    move(16,1)
    hline(ACS_HLINE,18)
    move(18,1)
    hline(ACS_HLINE,18)

if(__name__=="__main__"):
    main()
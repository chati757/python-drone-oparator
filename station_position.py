from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    #-----------determate window---------------
    start_color()#default is white
    noecho()#not show txt when typing
    curs_set(False)#not show cursor
    keypad(stdscr,True)#register arrow key 

    #-------------draft window------------------
    #draftwin(stdscr)
    #center(79 25) all(158 50) work space (154 44)
    #position panel(80 22)
    #-------------------------------------------

    max_y,max_x=getmaxyx(stdscr)
    #-----------create position panel-----------
    create_slot((max_y-28),(max_x-84))

    running = True
    while(running):
        key=getch()#don't forget setting window2 or window in this line
        if(key==27):
            running = False
            break

    endwin() #for stop ncurses

    return 0

def draftwin(stdscr):
    max_y,max_x=getmaxyx(stdscr)
    move(max_y/2,max_x/2)
    addstr("[ @ ]"+"center x= "+str(max_x/2)+" center y= "+str(max_y/2))
    move((max_y/2)+1,(max_x/2))
    addstr("[max colums x= "+str(max_x)+" max rows y= "+str(max_y)+"]")

def create_slot(y_axis,x_axis):
    #-------------station slot panel-----------
    #total width 80 high 22
    window_slot=newwin(22,80,0,0)
    box(window_slot)
    wmove(window_slot,0,35)
    waddstr(window_slot," POSITION ")

    #-------------station slot node------------
    #total width 20  high 22
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
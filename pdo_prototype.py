from unicurses import * 

#-----------------------------------------initalize stage----------------------------------------------
stdscr = initscr() #start up screen and initalize ncurses
#-----------determate default window---------------
start_color()#default is white
noecho()#not show txt when typing
curs_set(False)#not show cursor
keypad(stdscr,True)#register arrow key 

#-----------------layout--------------------
MAX_Y,MAX_X=getmaxyx(stdscr)

#-----------------main panel----------------
MAIN_STATION_MARGIN_TOP=1

#----------position panel layout------------
#size high 22 width 80 
#position x = 154-80 = 74
#position y = 44/2 = 22
POSITION_PANEL_SIZE_WIDTH=80
POSITION_PANEL_SIZE_HIGH=22
POSITION_PANEL_POS_Y=((MAX_Y-6)/2)
POSITION_PANEL_POS_X=((MAX_X-4)-POSITION_PANEL_SIZE_WIDTH) 
POSITION_MARGIN_TOP=2

def main():
    #-------------draft window------------------
    #draftwin(stdscr)
    #center(79 25) all(158 50) work space (154 44)
    #-------------------------------------------
    #-----------create main station-------------
    create_main_station()
    #-----------create position panel-----------
    create_main_position_panel()
    create_sub_position_panel("01","T01","NAME01","xxx%","Maintenance","offline",0)
    create_sub_position_panel("02","T02","NAME02","xxx%","Maintenance","offline",20)
    create_sub_position_panel("03","T03","NAME03","xxx%","Maintenance","offline",40)
    create_sub_position_panel("04","T04","NAME04","xxx%","Maintenance","offline",60)

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
    waddstr(window_sub_slot,"batt. "+batt_data)
    wmove(window_sub_slot,15,1)
    whline(window_sub_slot,ACS_HLINE,18)
    wmove(window_sub_slot,16,2)
    waddstr(window_sub_slot,status_data)
    wmove(window_sub_slot,17,1)
    whline(window_sub_slot,ACS_HLINE,18)
    wmove(window_sub_slot,18,2)
    waddstr(window_sub_slot,conn_data)

    #window_sub_slot_2=newwin(21,20,0,0)
    #box(window_sub_slot_2)
    
    #-------------all panel component----------
    wss_panel=new_panel(window_sub_slot)

    #wss_panel_2=new_panel(window_sub_slot_2)

    #-------------manage panel position--------
    move_panel(wss_panel,POSITION_MARGIN_TOP+1,POSITION_PANEL_POS_X+pos)

    #move_panel(wss_panel_2,1,20)

    #-------------panel update stage-----------
    update_panels()
    doupdate()

if(__name__=="__main__"):
    main()
#!/usr/bin/env python
#-*-coding: utf-8 -*-
from unicurses import * 
from make_color import *

#-----------------------------------------initalize stage----------------------------------------------
stdscr = initscr() #start up screen and initalize ncurses
#-----------determate default window---------------
start_color()#default is white
use_default_colors()
noecho()#not show txt when typing
curs_set(False)#not show cursor
keypad(stdscr,True)#register arrow key 

#-----------------initialize color themes----------
#default initialize color number
GREENLIGHT=new_color(COLOR_GREEN,COLOR_GREEN)
REDLIGHT=new_color(COLOR_RED,COLOR_RED)

#-----------------layout--------------------
MAX_Y,MAX_X=getmaxyx(stdscr)

#----------position panel layout------------
#size high 22 width 80 
#position x = 154-80 = 74
#position y = 44/2 = 22
POSITION_PANEL_SIZE_WIDTH=80
POSITION_PANEL_SIZE_HIGH=22
POSITION_PANEL_POS_Y=((MAX_Y-6)/2)
POSITION_PANEL_POS_X=((MAX_X-4)-POSITION_PANEL_SIZE_WIDTH) 
POSITION_MARGIN_TOP=2
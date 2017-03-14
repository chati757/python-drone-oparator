#!/usr/bin/env python
#-*-coding: utf-8 -*-
from unicurses import * 
from make_color import *
#declare for testing station_position.py
from station_init import *

def main():
    window_main_info=newwin(1,1,10,10)
    #box(window_main_info)
    hline(ACS_HLINE,11)
    vline(ACS_VLINE,11)
    panel=new_panel(window_main_info)
    update_panels()
    doupdate()
    endwin()

if(__name__=="__main__"):
    main()
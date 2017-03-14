#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unicurses import *
from station_init import *

trans_array=[["32"," "],["220","="],["10","\n"],["218","tl"],["196","-"]
,["191","tr"],["179","|"],["219","O"],["192","bl"],["217","br"]]

trans_txt=""

def Main():
    ascii_txt=[]
    global trans_txt=""
    #f=open("C:\Windows\System32\drivers\etc","a") append type 
    f = open("prototype_pos_logo_d01.txt","r")
    lines = f.readlines()
    print("all line")
    print(lines) #['list1\n','list2\n','list3']

    #input stage
    count=-1
    for line in lines:
        print("line")
        print(convert_to_ascii(line))
        ascii_txt+=str(convert_to_ascii(line)).split()
            
    f.close()
    print(ascii_txt)
    #output stage
    for txt in ascii_txt:
        for checkch in trans_array:
            if ((txt==checkch[0]) and (count<(len(ascii_txt)-1))):
                count=count+1 
                trans_txt+=txt.replace(checkch[0],checkch[1])

    print(trans_txt)
    print("test")

def convert_to_ascii(text):
    return " ".join(str(ord(char)) for char in text)

def convert_to_txtimage():
    window_main_info=newwin(1,1,10,10)
    #box(window_main_info)
    hline(ACS_HLINE,11)
    vline(ACS_VLINE,11)
    panel=new_panel(window_main_info)
    update_panels()
    doupdate()
    endwin()

if __name__=="__main__":
    Main()
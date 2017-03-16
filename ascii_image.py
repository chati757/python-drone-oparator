#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unicurses import *
from make_color import *

#use for debug mode
#from station_init import *

trans_array=[["32"," "],["220","="],["10","n"],["218","a"],["196","-"]
,["191","b"],["179","|"],["219","o"],["192","d"],["217","c"]]


def trans_image(path):
    ascii_txt=[]
    trans_txt=[]
    #f=open("C:\Windows\System32\drivers\etc","a") append type 
    f = open(path,"r")
    lines = f.readlines()
    #print("all line")
    #print(lines) #['list1\n','list2\n','list3']

    #input stage
    count=-1
    for line in lines:
        #print("line")
        #print(convert_to_ascii(line))
        ascii_txt+=str(convert_to_ascii(line)).split()
            
    f.close()
    #print(ascii_txt)
    for txt in ascii_txt:
        for checkch in trans_array:
            if ((txt==checkch[0]) and (count<(len(ascii_txt)-1))):
                count=count+1 
                trans_txt+=txt.replace(checkch[0],checkch[1])

    #print(trans_txt)
    #print("test")
    return trans_txt

def convert_to_ascii(text):
    return " ".join(str(ord(char)) for char in text)

def wconvert_to_txtimage(window,vl,hl,re_trans_text):
    global trans_array
    
    local_trans_text = re_trans_text
    hline_num=hl
    vline_num=vl

    for trch in local_trans_text:
        if(trch=="-"):
            wmove(window,vline_num,hline_num)
            whline(window,ACS_HLINE,1)
            hline_num+=1
        elif(trch=="n"):
            vline_num+=1
            hline_num=2
        elif(trch=="o"):
            wmove(window,vline_num,hline_num)
            waddstr(window,"  ",color_pair(new_color(14,14)))
            hline_num+=1
        elif(trch=="|"):
            #addstr("in|")
            wmove(window,vline_num,hline_num)
            wvline(window,ACS_VLINE,1)
            hline_num+=1
        elif(trch=="a"):
            #addstr("[tlin]")
            wmove(window,vline_num,hline_num)
            whline(window,ACS_ULCORNER,1)
            hline_num+=1
        elif(trch=="b"):
            #addstr("[trin]")
            wmove(window,vline_num,hline_num)
            whline(window,ACS_URCORNER,1)
            hline_num+=1
        elif(trch=="d"):
            #addstr("[blin]")
            wmove(window,vline_num,hline_num)
            whline(window,ACS_LLCORNER,1)
            hline_num+=1
        elif(trch=="c"):
            #addstr("[brin]")
            wmove(window,vline_num,hline_num)
            whline(window,ACS_LRCORNER,1)
            hline_num+=1
        else:
            wmove(window,vline_num,hline_num)
            waddstr(window,trch)
            hline_num+=1


if __name__=="__main__":
    #testing function. How to call ascii_image function
    window_main_info=newwin(10,20,0,0)
    box(window_main_info)
    wconvert_to_txtimage(window_main_info,2,2,DRONE_IMAGE_1)
    panel=new_panel(window_main_info)
    update_panels()
    doupdate()
    endwin()
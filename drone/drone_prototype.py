#!/usr/bin/env python
#-*-coding: utf-8 -*-
'''
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,True)
GPIO.output(7,False)
GPIO.cleanup()
'''
class drone_prototype:
    def __init__(self,id,name,pinmotor_r,pinmotor_l,pinsensor_trackline):
        self.id = id    
        self.name = name
        self.pinmotor_r = pinmotor_r
        self.pinmotor_l = pinmotor_l
        self.pinsensor_trackline = pinsensor_trackline
    #basic ability for Drone
    def trackline(self):
        #return true,false             
        return "trackline.."
    def move(self):             
        return "move.."
    def stop(self):             
        return "stop.."
    def turn_back(self):
        return "turn back.."
    def turn_left(self):
        return "turn left.."
    def turn_right(self):
        return "turn right.."

class water_drone(drone_prototype):
    def pump(self):
        #
        return "pump.."


#!/usr/bin/env python
#-*-coding: utf-8 -*-
import redis 

redis=redis.StrictRedis(
        host='localhost', 
        port=6379, 
        db=0, 
        password=8182757
        )        
        
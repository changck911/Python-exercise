# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:50:53 2018

@author: HChang

@title: RW file
"""

import os;

path = os.path.abspath('.\\data');

if not os.path.isdir(path):
    os.mkdir(path);

f = open(path+'\\test.txt','w');
f.write('test123');
f.close();
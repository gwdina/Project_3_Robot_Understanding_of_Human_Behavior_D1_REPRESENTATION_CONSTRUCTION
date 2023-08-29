#!/usr/bin/python3    
import cmath
import string
import time
import random
import csv
import json
import numpy as np
import os
import math
from pathlib import Path
import matplotlib.pyplot as plt




# custom joints: center of shoulders: 3, right shoulder: 5, left sholder: 9, rightknee: 14, leftknee: 18


# joint 1 is the center for each frame 




center = []

table = {}

distance_rhand = [] #8 d1

distance_head = [] #4 d2

distance_lhand = [] #12 d3

distance_lfoot = [] #20 d4

distance_rfoot = [] #16 d5

####
angle_1 = [] #8-4

angle_2 = [] #4-12

angle_3 = [] #12-20

angle_4 = [] #20-16

angle_5 = [] #16-8


# custom joints: center of shoulders: 3, right shoulder: 5, left sholder: 9, rightknee: 14, leftknee: 18
def file_read(fname):
        with open(fname) as f:
                i = 1
                joints = []
                for line in f:
                    numbers_str = line.split()
                    numbers_float = [float(x) for x in numbers_str]

                    # frame, joint, x, y, z
                    if(numbers_float[1] == 1):
                        center.append(numbers_float)

                    elif (numbers_float[1] == 3):
                        joints.append(numbers_float)

                    elif (numbers_float[1] == 5):
                        joints.append(numbers_float)

                    elif (numbers_float[1] == 9):
                        joints.append(numbers_float)

                    elif (numbers_float[1] == 14):
                        joints.append(numbers_float)

                    elif (numbers_float[1] == 18):
                        joints.append(numbers_float)
                        jon = joints
                        table[i] = jon
                        i += 1
                        joints = []
                    
                        


                    
                   
         

# file_read('a08_s01_e01_skeleton_proj.txt')




#print(table)

def distance(frame,x,y,z):
    # do we need the center
    # result = math.sqrt(x**2 + y**2 + z**2)
    result = math.sqrt((x - center[frame][2])**2 + (y - center[frame][3])**2 + (z - center[frame][4])**2)
    #print(result)
    return result

def angle(x1,y1,z1,x2,y2,z2):
    top = x1*x2 + y1*y2 + z1*z2 
    bottom = math.sqrt((x1**2 + y1**2 + z1**2) * (x2**2 + y2**2 + z2**2))
    calc = top / bottom
    return math.acos(calc) * (180 / math.pi)

# custom joints: center of shoulders: 3, right shoulder: 5, left sholder: 9, rightknee: 14, leftknee: 18
def build_table():
    for keys in table.keys():
        distance_head.append(distance(keys-1, table[keys][0][2],table[keys][0][3], table[keys][0][4])) # center of shoulders: 3

        distance_rhand.append(distance(keys-1, table[keys][1][2],table[keys][1][3], table[keys][1][4])) # right shoulder: 5
    
        distance_lhand.append(distance(keys-1, table[keys][2][2],table[keys][2][3], table[keys][2][4])) # left sholder: 9

        distance_rfoot.append(distance(keys-1, table[keys][3][2],table[keys][3][3], table[keys][3][4])) # rightknee: 14

        distance_lfoot.append(distance(keys-1, table[keys][4][2],table[keys][4][3], table[keys][4][4])) # leftknee: 18

        # angles: 1 = 8-4, 2 = 4-12, 3 = 12-20, 4 = 20-16, 5 = 16-8 
        angle_1.append(angle(table[keys][1][2], table[keys][1][3], table[keys][1][4], table[keys][0][2], table[keys][0][3], table[keys][0][4])) # 5-3

        angle_2.append(angle(table[keys][0][2], table[keys][0][3], table[keys][0][4], table[keys][2][2], table[keys][2][3], table[keys][2][4])) # 3-9

        angle_3.append(angle(table[keys][2][2], table[keys][2][3], table[keys][2][4], table[keys][4][2], table[keys][4][3], table[keys][4][4])) # 9-18

        angle_4.append(angle(table[keys][4][2], table[keys][4][3], table[keys][4][4], table[keys][3][2], table[keys][3][3], table[keys][3][4])) # 18-14

        angle_5.append(angle(table[keys][3][2], table[keys][3][3], table[keys][3][4], table[keys][1][2], table[keys][1][3], table[keys][1][4])) # 14-5


file = open("cust_d1_test.txt", "w")
file.close()

Path = "dataset/test/"
filelist = os.listdir(Path)
for i in filelist:
    if i.endswith(".txt"):
        # print(Path+i)
        file_read(Path+i)
        build_table()

        fix1 = np.array(distance_rhand)
        d1, bin1 = np.histogram(fix1[~np.isnan(fix1)])

        d1  = d1 / len(table)

        fix2 = np.array(distance_head)
        d2, bin2 = np.histogram(fix2[~np.isnan(fix2)])

        d2  = d2 / len(table)

        fix3 = np.array(distance_lhand)
        d3, bin3 = np.histogram(fix3[~np.isnan(fix3)])
        
        d3  = d3 / len(table)

        fix4 = np.array(distance_lfoot)
        d4, bin4 = np.histogram(fix4[~np.isnan(fix4)])

        d4  = d4 / len(table)

        fix5 = np.array(distance_rfoot)
        d5, bin5 = np.histogram(fix5[~np.isnan(fix5)])

        d5  = d5 / len(table)

        fix_angle_1 = np.array(angle_1)
        theta1, bin6 = np.histogram(fix_angle_1[~np.isnan(fix_angle_1)])

        theta1  = theta1 / len(table)

        fix_angle_2 = np.array(angle_2)
        theta2, bin7 = np.histogram(fix_angle_2[~np.isnan(fix_angle_2)])

        theta2  = theta2 / len(table)

        fix_angle_3 = np.array(angle_3)
        theta3, bin8 = np.histogram(fix_angle_3[~np.isnan(fix_angle_3)])

        theta3  = theta3 / len(table)

        fix_angle_4 = np.array(angle_4)
        theta4, bin9 = np.histogram(fix_angle_4[~np.isnan(fix_angle_4)])

        theta4  = theta4 / len(table)

        fix_angle_5 = np.array(angle_5)
        theta5, bin10 = np.histogram(fix_angle_5[~np.isnan(fix_angle_5)])

        theta5  = theta5 / len(table)

        con = np.concatenate((d1, d2, d3, d4, d5, theta1, theta2, theta3, theta4, theta5))
        file = open("cust_d1_test.txt", "a")
        file.write(i[:11])
        file.write(": ")
        file.write(" ".join([str (x) for x in con]))
        file.write('\n')
        file.close()
        
        center = []
        table = {}
        distance_rhand = [] #d1
        distance_head = [] #d2
        distance_lhand = [] #d3
        distance_lfoot = [] #d4
        distance_rfoot = [] #d5
        ####
        angle_1 = [] #5-3
        angle_2 = [] #3-9
        angle_3 = [] #9-18
        angle_4 = [] #18-14
        angle_5 = [] #14-5
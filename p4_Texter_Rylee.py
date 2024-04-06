#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:39:22 2024

@author: ryleetexter
"""

#Rylee Texter
#Problem 4: Function Visualization
import math
import matplotlib.pyplot as plt

#taking input for equation, minimum, maximum, and number of points

fun_str = input("Enter function with Variable x: ")
mini = float(input("Enter the minimum domain: "))
maxi = float(input("Enter the maximum domain: "))
min_max = (mini, maxi)
ns = int(input("please enter the amount of points on the graph: "))



def plot_function(fun_str, min_max, ns):
    xs = []
    ys = []
    
    ##min max and difference between xs (dx)
    d0 = min_max[0]
    d1 = min_max[1]
    dx = (d1-d0)/ns
    
    x = d0
    
    #adding the xs based on the ns
    while x <= d1:
        xs.append(x)
        x+=dx
        
        
    #appending the ys based on what the user input
    #and based on the ns
    for x in xs:
        y = eval(fun_str)
        ys.append(y)
    
    
    #formatting the table
    print("{:>10} {:>10}".format('X', 'Y'))
    print("- "*12)
   
    #looping through the xs and ys and printing them to the console
    for i in range(len(xs)):
        print("{:>10.3f} {:>10.3f}".format( xs[i],  ys[i]))
        
        
    ##creating a graph with title, labels, and plotted points
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(fun_str)
    plt.plot(xs, ys)
       
            
        
plot_function(fun_str, min_max, ns)
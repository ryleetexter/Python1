#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 18:08:11 2024

@author: ryleetexter
"""

#Rylee Texter
#Problem 3: Duplicated Substrings

def find_dup_str(s,n):
    #counters for current of frist and last indexes of the current substring
    current_start = 0
    current_stop = n
    current_substring = s[current_start:current_stop]
    
    #loop changes the current substring and updates counters
    for i in range(len(s)-n+1):
        
        #loops through the rest of the string to check if there is a match
        for j in range(len(s)-n+1):
            if (s[j:j+n] == current_substring):
                
                #ensures that the duplicate string is not overlap
                if (j > current_stop):  
                    return(current_substring)
        current_start += 1
        current_stop += 1
        current_substring = s[current_start:current_stop]
        
        
def find_max_dup(s):
    #loops through the length of the string to 2 to find the largest match first
    for i in range(len(s), 1, -1):
        
        #checks if there is a match
        if find_dup_str(s, i) != None:
            print(find_dup_str(s, i))
            break
        
        #there was no match
        elif i == 2:
            print(" none ")

    

string_input = input("Hi there. Please enter any phrase you would like: ")
#length_input = int(input("Also enter an integer length: "))

#print(find_dup_str(string_input, length_input))

find_max_dup(string_input)

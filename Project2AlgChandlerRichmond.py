# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:10:07 2022

@author: CJRICH
"""
#Arranged by Chandler Richmond for Algorithms Hu CSCI 3330
import math 
import time
import numpy as np
import sys

first = 1
second = 2
third = 3
fourth = 4
fifth = 5


#Create Array from textfile (next two code blocks)
#https://www.codespeedy.com/create-an-array-from-a-txt-file-in-python/
def generatelist():
   list1=np.loadtxt("generated.txt",dtype="int")
   return list1

def generatelist2():
   list1=np.loadtxt("generated.txt",dtype="int")
   return list1

list1 = generatelist()
unsortedlist = generatelist2()
#list1 = [9,3,4,5,6]

    
def prompt():
    print ("Which sorting algorithm would you like to test today?")
    print ("1. Bubble Sort \n2. Merge Sort \n3. Quick-Sort \n4. Insertion Sort \n5. Exit")
    
    
    
##Bubble Sort
#Original contributor for Bubble Sort Code below
#JavaTPoint
#https://www.javatpoint.com/bubble-sort-in-python

    # Creating a bubble sort function  
def bubble_sort(list1):  
        # Outer loop for traverse the entire list  
        for i in range(0,len(list1)-1):  
            for j in range(len(list1)-1):  
                if(list1[j]>list1[j+1]):  
                    temp = list1[j]  
                    list1[j] = list1[j+1]  
                    list1[j+1] = temp  
        return list1  
    
    
#Merge Sort
#Original Contributor for Merge Sort Code Below
#Medium.com
#https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
def merge_sort(list1):
    # The last array split
    if len(list1) <= 1:
        return list1
    mid = len(list1) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(list1[:mid]), merge_sort(list1[mid:])

    # Merge each side together
    return merge(left, right, list1.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


##Quick Sort
#Original Contributor for Quick Sort Code Below
#Brilliant.org
#https://brilliant.org/wiki/quick-sort/

def quickSort(list1):
    less = []
    pivotList = []
    more = []

    if len(list1) <= 1:
        return list1
    else:
        pivot = list1[0]
        for i in list1:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more




    

    
##Insertion Sort
#Original Contributor for Insert Sort Code Below
#Brilliant.org
#https://brilliant.org/wiki/insertion/
def insertion_sort(list1):
    for slot in range(1, len(list1)): 
        value = list1[slot]
        test_slot = slot - 1
        while test_slot > -1 and list1[test_slot] > value:
            list1[test_slot + 1] = list1[test_slot]
            test_slot = test_slot - 1
        list1[test_slot + 1] = value
    return list1


    
 
def choose_sort():
    
    if choice == first:
        startTime = time.time()
        sortedlist = bubble_sort(list1)
        executionTime = (time.time() - startTime)
        print("You have chosen Bubble Sort!")
        print("After sorting the array of integers in the text file,")
        print ("The Bubble Sort finished in " + str(executionTime) +" seconds\n")
        return sortedlist
        
        
    elif choice == second:
        startTime = time.time()
        sortedlist = merge_sort(list1)
       # print ("The Merge Sorted List is: ", list1)
        executionTime = (time.time() - startTime)
        print("You have chosen Merge Sort!")
        print("After sorting the array of integers in the text file,")
        print ("The Merge Sort finished in " + str(executionTime) + " seconds\n")
        return sortedlist
    
    elif choice == third:
        startTime = time.time()
        sortedlist =  quickSort(list1)
       # print ("The Merge Sorted List is: ", list1)
        executionTime = (time.time() - startTime)
        print("You have chosen Quick Sort!")
        print("After sorting the array of integers in the text file,")
        print ("This Quick Sort finished in " + str(executionTime) + " seconds\n")
        return sortedlist
       
        
    elif choice == fourth:
        startTime = time.time()
        sortedlist = insertion_sort(list1)
        #print ("The Insertion Sorted List is: ", list1)
        executionTime = (time.time() - startTime)
        print("You have chosen Insertion Sort!")
        print("After sorting the array of integers in the text file,")
        print ("This Insertion Sort finished in " + str(executionTime) + " seconds\n")
        return sortedlist
    elif choice == fifth:
        dummyvariable = 0
    else:
        print ("Your choice was invalid. Try Again 1-5")
        
        
        
##MAIN DRIVER PROGRAM        
choice = 0  
print ("Welcome to Project 2 where we compare Sorting Algorithims!! YAY")
print ("The sorting algorithims below will be sorting an array of 1000 randomly generated numbers\n")   


while choice != fifth: 
    prompt()
    list1 = unsortedlist
   # list1 = [9,3,4,5,6]
    choice = int(input())
    #print("The Unsorted list is: ", unsortedlist) 
    sortedlist = choose_sort()
    #print("The Sorted list is: ", sortedlist) 
    print("\n")
    
    
print ("Thank You for using this Program! - CJRICH")  
raise SystemExit(0)  
        


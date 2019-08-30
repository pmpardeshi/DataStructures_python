#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 4 23:30:48 2019

@author: pmpardeshi
"""

def merge(arr,low,middle,high):
    leftArray=[]
    rightArray=[]
    mergearr=[0]*(high+1)
    #calculating differences bteween left middle and right 
    #will exclude middle both the times
    #thus add 1 to first difference
    
    leftArrSize=middle-low+1
    rightArrSize=high-middle
    
    for i in range(leftArrSize):
        leftArray.append(arr[low+i])
    
   # print(f"left array {leftArray}") uncomment these statements to understnd working of merge function

    for j in range(rightArrSize):
        rightArray.append(arr[middle+1+j])
    
    #print(f"right array {rightArray}")

    i=j=0
    k=low
    #loop untill any one array is exhausted
    while(i<leftArrSize and j<rightArrSize):
        if leftArray[i]<=rightArray[j]:
            mergearr[k]=arr[k]=leftArray[i]
            i=i+1
            
        else:
            mergearr[k]=arr[k]=rightArray[j]
            j=j+1
        k=k+1
            
    #exhaust remaining array        
    while i<leftArrSize:
         mergearr[k]=arr[k]=leftArray[i]
         i=i+1
         k=k+1
         
    while j<rightArrSize:
        mergearr[k]=arr[k]=rightArray[j]
        j=j+1
        k=k+1
        
    #print(f"merge array {mergearr}")
            

def merge_sort(arr,low,high):
    if low<high:
        middle=int(low+(high-low)/2)
        merge_sort(arr,low,middle)
        merge_sort(arr,middle+1,high)
        merge(arr,low,middle,high)
        

if __name__=="__main__":
    arr=[int(x) for x in input("enter array").split()]
    n=len(arr)
    merge_sort(arr,0,n-1)
    print(f"Sorted{arr}")

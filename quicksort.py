# -*- coding: utf-8 -*-
"""
Created on Sat Aug 3 23:36:25 2019

@author: pmpardeshi
"""
#our aim with partitioning is to collect all elements smaller than pivot to left
#thus all elements larger than pivot is at right
def partition(arr,low,high):
    pivot=arr[high] #last element as pivot
    i=low-1  #i will point to the most recent element smaller than pivot
    
    
    for j in range(low,high):
        if arr[j] <= pivot: #arr[j] is smaller than pivot
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
            
    #j came to an end 
    #i points to the last smaller element
#hence i+1 must be greater then pivot 
#hence upon swapping we get two partitions        
    arr[high],arr[i+1]=arr[i+1],arr[high]
    return (i+1)

def quicksort(arr,low,high):
    
    if low < high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
        
if __name__=='__main__':
    arr=[int(x) for x in input("enter data:\t").split()]
    n=len(arr) 
    quicksort(arr,0,n-1)
    print(arr)
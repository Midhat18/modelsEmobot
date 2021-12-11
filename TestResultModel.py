# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 03:05:10 2021

@author: HP
"""

import pandas as pd
from numpy import *
import numpy as np


def TestResult(answersArray):
#test data file read 
    data = pd.read_csv('Test_Anxiety.csv')
    result = ''
    
#Changing to array
    array = data.values
#print(array)
    fileRows= len(array)
#print(array)

#using numpy class for creating dataframe
    df = pd.DataFrame(array)
    print(df.head())

#Testfile Required index selection extracting irrelevant indexes
    maindf = df[[ 2, 3, 4, 5, 6,7,8,9]]

#again conversion to 2D array
    mainarray = maindf.values
    print(mainarray)

#Array splitting
    arr=np.array(mainarray)
    arr.shape
    arr3=np.split(arr,fileRows)

#Counter save value of matches
    counter=0
#Maximun match in a row count
    count=0

#pattern matched array store in here
    arrarResult=[]

#Input array
    array1= answersArray
#File Data
#['male' 25 1 1 2 1 2 2 2 'moderate']
# ['female' 20 2 1 2 2 2 2 2 'moderate']
# ['female' 17 1 2 2 2 2 2 2 'moderate']
 #['male' 27 2 1 1 1 1 2 1 'mild']
 #[#'female' 29 1 2 2 1 1 2 1 'mild']
 #['#male' 30 3 2 2 1 2 2 2 'moderate']
# ['m#ale' 22 2 3 3 2 2 3 3 'severe']
# ['male' 28 3 3 3 3 3 3 3 'severe']
# ['female' 30 1 1 2 2 1 2 2 'moderate']
# ['male' 20 3 2 1 1 1 2 2 'mild']#

#pattern matching

    for i in range(len(arr3)):
        arr5=arr3[i]
        print(arr5)
        arr8=arr5[0]
        print(arr8)
    #print(len(arr8))
        for j in range(len(arr8)-1):
        #print(i,j)
            if int(arr8[j])==array1[j]:
                print(array1[j],arr8[j])
                counter+=1
                print("Counter value",counter,"count value",count)
                arr9=arr8
        
    
        if counter>count:
            count=counter
            arrayResult=arr9
            print(arrayResult)
        else:
            count=count
        counter=0



    print(arrayResult)
    arrlen =len(arrayResult)
    result = arrayResult[arrlen-1]
    print("you have ",arrayResult[arrlen-1],"Anxiety")
    return result
#print(count)


    

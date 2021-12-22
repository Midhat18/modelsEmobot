

import pandas as pd
from numpy import *
import numpy as np


def TestResult(answersArray):
    mainarray=[]
    testName=''
    
    
    if len(answersArray)==7:
        #test data file read 
        data = pd.read_csv('Test_Anxiety.csv')
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
        testName = "Anxiety"
    else:
        data = pd.read_csv('Patient_Health_Questionnaire.csv')
        #Changing to array
        array = data.values
    #print(array)
        fileRows= len(array)
    #print(array)

    #using numpy class for creating dataframe
        df = pd.DataFrame(array)
        print(df.head())

    #Testfile Required index selection extracting irrelevant indexes
        maindf = df[[ 2, 3, 4, 5, 6,7,8,9,10,11,12,13]]

    #again conversion to 2D array
        mainarray = maindf.values
        testName = "Depression"
        
       
    return processResult(mainarray,answersArray,fileRows,testName)
#print(count)


def processResult(array,array2,filerow,testName):
    arrarResult=[]
    result = ''
    counter=0
    count=0
    print(array)

#Array splitting
    arr=np.array(array)
    arr.shape
    arr3=np.split(arr,filerow)
#pattern matched array store in here
    

#Input array
    array1= array2
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
    result = arrayResult[arrlen-1]+testName
    print(result)
    
    return result

    

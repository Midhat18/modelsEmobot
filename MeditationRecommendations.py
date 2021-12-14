# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from numpy import *
import numpy as np
def recommended_meditation(healthissue,medi_rec):
    data = pd.read_csv('c:/Users/DELL/Desktop/meditation_filtering.csv')
    data1 = pd.read_csv('c:/Users/DELL/Desktop/health_issue.csv')
    health_issue_file_data =data1.values
    meditation_file_data = data.values
    meditation_files_entries = len(meditation_file_data)
    data_frame = pd.DataFrame(meditation_file_data)
    df = pd.DataFrame(health_issue_file_data)
    extrc_colmn= df[[1,2,3,4,5,6]]
    save_medi_result=[]
    meditations=[]
    print(data1.columns)
    extrac_co = data_frame[[0]]
    #print(extrac_co)
    extracted_columns = data_frame[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
    extracted_columns_values = extracted_columns.values
    #print(extracted_columns_values)
    Single_meditation_values = np.array(extracted_columns_values)
    Single_meditation_values.shape
    #print(Single_meditation_values)
    single_meditation = np.split(Single_meditation_values, meditation_files_entries)
    #print(single_meditation)
    health_issue =healthissue
    userRating = medi_rec
    store = 0
    store_1 = 0
    save = []
    final12 = []
    counter = 0
    i = len(Single_meditation_values)
    recommended_meditation_array = []
    for meditation in range(len(Single_meditation_values)):

        meditation_1 = Single_meditation_values[meditation]

        print(meditation_1)

        # print(len(userRating))

        # print(userRating[user - 1])
        for me in range(len(userRating)):
            # print("Meditation ", medii_1[me], "index ", me)
            #print("user ", meditation_1[me])
            store = meditation_1[me] * userRating[me]
            #print("Multiplication Result ", store)
            store_1 = store + store_1
            #print(store_1)

        save.append(store_1)
        #print(store_1)
        store_1 = 0

    #print(save)
    recommended_meditation = save[0]
    for compare_meditation in range(len(save)):

        # print(initial_meditation)

        if save[compare_meditation] > recommended_meditation:
            recommended_meditation = save[compare_meditation]
            recommended_meditation_array.append(recommended_meditation)


    print("Here is your recommended meditation", recommended_meditation)

    for check_val in range(len(save)):
        if recommended_meditation == save[check_val]:
            counter = counter + 1
            final12.append(check_val )
    #print(final12)
    #print(len(final12))

    print("recommended meditation categories are")
    if len(final12)>1:
        for result in range(len(final12)):
            indexValue = final12[result]
            for result2 in range(len(extrac_co)):
                save_medi = extrac_co[0]
                if result2 == indexValue:
                    #print(save_medi[indexValue])
                    save_medi_result.append(save_medi[indexValue])


    else:

        rec = final12[0]
        for result2 in range(len(extrac_co)):
            save_medi1 = extrac_co[0]
            if result2 == rec:
                #print(save_medi1[rec])
                save_medi_result.append(save_medi1[rec])


    #print(save_medi_result)
    track_index = -1
    healthisuue_array=[]

    for col in data1.columns:
        track_index= track_index+1
        if health_issue==col:
           catg_medi= extrc_colmn[track_index]
           for ctg in range(len(catg_medi)):

               if catg_medi[ctg] == 1:
                   print(ctg)
                   print(df[0][ctg])
                   healthisuue_array.append(df[0][ctg])

    coun=0

    #print(healthisuue_array)

    meditation_content_length = len(save_medi_result)
    healthissue_length = len(healthisuue_array)
    meditation1=[]
    meditation1 = save_medi_result + healthisuue_array
    meditations = list(dict.fromkeys(meditation1))


    return meditations

#print(meditations)









# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

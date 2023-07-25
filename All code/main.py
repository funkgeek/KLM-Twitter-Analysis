import pandas as pd
import os
import time
import json
from frames_functions import *

'''
Place all jsons that you want to be converted inside of the base_dir

Let run for a while, you should see print statements stating progress
'''



base_dir = '/Users/rong/Desktop/School Q4/DBL/project/data'

failed = []

frame = 0



def NewFrame (Data):
    global frame
    global Megaframe
    framename = 'frame ' + str(frame) + '.csv'
    frame += 1
    Data.to_csv(framename)
    del Megaframe
    print('Dataframe stored under name ' + framename + ' and megaframe wiped')





for file in os.listdir(base_dir):
    start_time = time.time()

    json_path = os.path.join(base_dir, file)
    try:
        json_data = pd.read_json(json_path, lines=True)
    except:
        print('Failed to open ' +  json_path + ', initiating recovery')
        failed.append(json_path)
        json_data = corruptedfilerecovery([json_path])


    try:
        Megaframe = pd.concat([Megaframe,json_data])
    except:
        Megaframe = json_data
    elapsed = time.time()-start_time
    print('Finished loading ' + str(106 - os.listdir(base_dir).index(file)) + ' ' + json_path + ' in ' + str(elapsed) + ' seconds')
    if (os.listdir(base_dir).index(file) + 1) % 10 == 0:
        NewFrame(Megaframe)





NewFrame(Megaframe)




with open("file.txt", "w") as output:
    for i in failed:
        output.write(str(i)+',')
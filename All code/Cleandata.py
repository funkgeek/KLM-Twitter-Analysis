import pandas as pd
import pandas as pd
import os
import time
import json
import ast
from frames_functions import *

frame = 0

'''
Place all dataframes that you want to be cleaned inside of the base_dir

Let run for a while, you should see print statements stating progress
'''

base_dir = '/Users/david/Desktop/School Q4/DBL/project/Dataframes'
for file in os.listdir(base_dir):
    start_time = time.time()
    dataframe_path = os.path.join(base_dir, file)
    df_twitter = pd.read_csv(dataframe_path)
    df_twitter = CleanColumns(df_twitter)
    df_twitter = TestUser(df_twitter)
    print(df_twitter.columns)
    df_twitter = df_twitter[['user_id','id','text','created_at','in_reply_to_status_id','in_reply_to_user_id']]


    filename = 'clean frame ' + str(frame) + '.csv'
    frame += 1
    df_twitter.to_csv(filename)

    elapsed = time.time()-start_time
    print('Cleaned frame '+ str(frame) + ' in ' + str(elapsed) + ' seconds')

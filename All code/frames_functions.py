import pandas as pd
import json
import time
import ast

def ApplyThis(x):
    try:
        return ast.literal_eval(x)
    except:
        print('error tweet')

def ApplyThis2(x):
    try:
        return x.get('id')
    except:
        print('error tweet')

def TestUser(dataframename):
    df = dataframename
    df['user_dict'] = df['user'].apply(lambda x: ApplyThis(x))
    df['user_id'] = df['user_dict'].apply(lambda x: ApplyThis2(x))
    df.drop(columns=['user_dict','user'])
    return df

def CleanColumns(dataframename):
    df = dataframename
    df = df.drop(columns=['id_str','display_text_range','source','in_reply_to_status_id_str','in_reply_to_user_id_str',
                     'geo','coordinates','place','contributors','extended_entities','favorited','retweeted','delete',
                     'possibly_sensitive','filter_level','timestamp_ms'])
    return df


def UserInfo(dataframename):
    df_tweets = dataframename
    length = df_tweets.shape[0]
    for i in range(length):
        try:
            df = df_tweets.loc[i,'user']
            user_dict = (ast.literal_eval(df))
            df_tweets.loc[i,'user_id'] = user_dict['id']
            df_tweets.loc[i,'user_name'] = user_dict['name']
            df_tweets.loc[i,'user_location'] = user_dict['location']
        except:
            print('error tweet',length - i)
    return df_tweets


def corruptedfilerecovery(filenames):

    extratweets = []
    failedtweets = 0

    for i in filenames:
        file = open(i)
        tweets = file.readlines()
        for j in tweets:
            try:
                extratweets.append(json.loads(j))
            except:
                failedtweets += 1

    extraframe = pd.DataFrame.from_records(extratweets)
    print('Finished recovery with ' + str(failedtweets) + ' removed tweets')
    return extraframe





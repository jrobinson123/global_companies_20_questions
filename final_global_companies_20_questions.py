
#import needed modules
import pandas as pd
import numpy as np
import random

#load the csv file and convert it to a DataFrame
file_name = "global_500_companies.csv"
df = pd.read_csv(file_name)

#creation of the Region column
df["Region"] = [hq[hq.index(",")+2:] for hq in df["HQLocation"]]

#make a list of keys for the DataFrame
keys = ["Sector","Region","CompanyName","HQLocation"]

#bool that can break out of the main loop if the company is guessed
company_guessed = False

#asks the user a question based on a key
def filter_by_key(dataf,key):
    key_list = dataf[key].tolist()
    choice = random.choice(key_list)
    question = "is it {}?".format(choice)
    user_input = input(question)

    if(user_input == "n" or user_input == "no"):
        dataf = dataf[(dataf[key] != choice)]
    elif(user_input == "y" or user_input == "yes"):
        if key == "CompanyName":
            dataf = dataf[(dataf[key] == choice)]
            global company_guessed
            company_guessed = True
        #checking for length of keys is potentially pointless
        elif(len(keys) > 1):
            dataf = dataf[(dataf[key] == choice)]
            keys.remove(key)

    return dataf


#main game loop
while True:
    key_choice = random.choice(keys)
    df = filter_by_key(df,key_choice)
    print(len(df))
    if(company_guessed == True):
        break

print(df)


#import needed modules
import pandas as pd
import numpy as np
import random

#load the csv file and convert it to a DataFrame
file_name = "global_500_companies.csv"
df = pd.read_csv(file_name)


# methods for the displaying the company names in a df
def displayCompanies(dataf):
    internal_companies = dataf["CompanyName"].tolist()
    return internal_companies

#method for displaying a message if only one company is left
#returns true if only one company is remaining
def displayCompaniesRemaining(dataf):
    internal_companies = dataf["CompanyName"].tolist()
    if(len(internal_companies)) == 1:
        print("Your company is {}" .format(dataf["CompanyName"]))
        return True
    return False

# grab a random company for testing
companyNames = df["CompanyName"].tolist()
randomCompany = random.choice(companyNames)
print(randomCompany)


#make a list of keys for the DataFrame
keys = ["Sector","HQLocation","CompanyName"]

#bool that can break out of the main loop
break_bool = False

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
            global break_bool
            break_bool = True
        elif(len(keys) > 1):
            keys.remove(key)
            dataf = dataf[(dataf[key] == choice)]

        # elif len(keys) == 1:
        #     #global break_bool
        #     break_bool = True

    return dataf

while True:
    key_choice = random.choice(keys)
    df = filter_by_key(df,key_choice)
    print(len(df))
    if(break_bool == True):
        break


print(df)


# while True:
#   temp_choice = generate_question()
#   print("is you company in{} sector".format(temp_choice))

# global_companies_20_questions
In this program, the computer will play a 20 questions style text-based game against you

[<title>](<link>)




https://github.com/cmusam/fortune500

### Dependencies
This program was written in python3, the libraries used are pandas,numpy, and random


### Usage
1) clone the script
2) using the terminal, go into the directory containing this script
3) run the program from the terminal

### code explained:
This program is a text based game. You start by choosing a company listed in the csv file. The company has properties such as the HQLocation, Sector, and of course CompanyName. The computer repeatidley will ask yes or no questions until it is able to guess the company you were thinking of. 

Here's a step-by-step guideline which shows how the code was created:

To start we import needed modules, then load in our csv file and make it a DataFrame using [pandas](https://pandas.pydata.org/)
```python
#import needed modules
import pandas as pd
import numpy as np
import random

#load the csv file and convert it to a DataFrame
file_name = "global_500_companies.csv"
df = pd.read_csv(file_name)¸
```
Some additional set-up is needed in terms of creating a list of keys, and a boolean to control loop breaking

```python
#make a list of keys for the DataFrame
keys = ["Sector","HQLocation","CompanyName"]

#bool that can break out of the main loop
break_bool = False
```
Here's the bones of the program

```python
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
            global break_bool
            break_bool = True
        elif(len(keys) > 1):
            keys.remove(key)
            dataf = dataf[(dataf[key] == choice)]

        # elif len(keys) == 1:
        #     #global break_bool
        #     break_bool = True

    return dataf
```
This is the definition of a function that will take in a DataFrame and a key as input. Then after taking in user input, the function will return a new, filtered DataFrame. In this case filtering is reffering to reducing the size of the DataFrame.

Here's the step-by-step
1) convert the DataFrame of the inputted key to a list
```python
    key_list = dataf[key].tolist()
```
2) set a variable called choice equal to random choice from this newly created list
```python
    choice = random.choice(key_list)
```
3) create a question variable, and then take in input from the user
```python
    question = "is it {}?".format(choice)
    user_input = input(question)
```

The input can be either "yes" or "no"
if input is no, then set the data frame equal to the data frame of not the choice
```python
   if(user_input == "n" or user_input == "no"):
        dataf = dataf[(dataf[key] != choice)]
```
if input is yes, then set the DataFrame equal to the DataFrame of choice
additionally if the input is yes and the key is "CompanyName" then the computer has sucessfully guessed the company and the break boolean should be set equal to true
if the key is not "CompanyName" then they key should be removed from the keys list, with the break boolean staying false
```python
    elif(user_input == "y" or user_input == "yes"):
        if key == "CompanyName":
            dataf = dataf[(dataf[key] == choice)]
            global break_bool
            break_bool = True
        elif(len(keys) > 1):
            dataf = dataf[(dataf[key] == choice)]
            keys.remove(key)
           
```





The last section of the program incorporates the previously defined data and function into a simple While True loop. 
```python
while True:
    key_choice = random.choice(keys)
    df = filter_by_key(df,key_choice)
    print(len(df))
    if(break_bool == True):
        break
       


print(df)
```
The loop starts by choosing a random key from the key list. From there, df and the random key will be plugged into the filter_by_key function, returning a new filtered df. If the break_bool is set to true in the function then the loop will be broken.

Finally, one last print statement prints out the entire df which at this point should only be one company. 




### To-Do
There are a few additions I'm interested in trying, here they are:

1) have the program ask questions based on other properties of the company such as profit, revenue, and number of employeees
2) I'm interested in this program taking in other data sets such as the Fortune 500 compared to the Global 500, it would be especially interesting with very large data sets
3) I want to create a reverse version where the computer choosed a company and you have ask it questions and eventually correctly guess the company it was thiknking of
4) add a weighted average to the random choice of keys in the main game loop

### References

### Insight/motivation:
This game effectively blends my interest with corporations and game strategy, In fact 20 questions with corporations is one of my favorite games to play with my family, however they aren't quite as interested as me. Creating this was a school project final. It is also personal passion project due to it's interesting requirement of logic, and cleverly sorting of data. 

 




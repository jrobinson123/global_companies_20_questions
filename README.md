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
This program is a text based game. You start by choosing a company listed in the csv file. The company has properties such as the headquarters, sectory, and of course companyname. The computer repeatidley will ask yes or no questions until it is able to guess the company you were thinking of. 

Here's a step-by-step guideline which shows how the code was created:
'''python
#import needed modules
import pandas as pd
import numpy as np
import random

#load the csv file and convert it to a DataFrame
file_name = "global_500_companies.csv"
df = pd.read_csv(file_name)¸
'''

### To-Do

### References

### Insight/motivation



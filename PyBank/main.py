# ## Option 1: PyBank
# ![Revenue](Images/revenue-per-lead.jpg)
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company.
#You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). 
#Each dataset is composed of two columns: `Date` and `Revenue`. 
#(Thankfully, your company has rather lax standards for accounting so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:

import os
import csv

revenue_data = {} # List to hold the revenues
Total_Revenue = 0 # initialize Total Revenue to Zero
months =[]
revenue = []
Average_Change = 0
reve_diff = []
file_path = input("Enter the file path: ")
with open(file_path, newline="") as csvfile: # open the csv file
    csvreader = csv.reader(csvfile, delimiter = ",") # read the csv file
    next(csvreader, None) # skip the header
    #loop thru each row and extract the data into a dictionary "revenue_data"
    for row in csvreader: 
        revenue_data[row[0]] = float(row[1])
    # calculate the average revenue change accross the data set 
    months = list(revenue_data.keys()) # import keys into list "Months"
    revenue = list(revenue_data.values()) # import values into list "revenue"
    if revenue[0] > revenue[len(revenue)-1] :
        Average_Change = (revenue[0]-revenue[len(revenue)-1]) / len(revenue)
    else :
        Average_Change = (revenue[len(revenue)-1] - revenue[0]) / len(revenue)
        
    # * The greatest increase & decrease in revenue (date and amount) over the entire period
    for i in range(len(revenue)-1) :
        reve_diff.append(revenue[i]-revenue[i+1])
    Inc_Rev = int(max(reve_diff))
    Dec_Rev = int(min(reve_diff))
    max_index = int(reve_diff.index(max(reve_diff)))
    min_index = int(reve_diff.index(min(reve_diff)))

print("-----------------------------------------------------------")
print("Financial Analysis")
print("-------------------------------------------------")
# * The total number of months included in the dataset        
print("Total Months: " + str(len(revenue_data)))
# * The total amount of revenue gained over the entire period
print("Total Revenue: $" + str(int(sum(revenue_data.values()))))
# * The average change in revenue between months over the entire period
print("Average Revenue Change: $" + str(int(Average_Change)))
# * The greatest increase in revenue (date and amount) over the entire period
print("Greatest Increase in Revenue: "+ months[max_index] + " ($" + str(Inc_Rev) + ")")
# * The greatest decrease in revenue (date and amount) over the entire period
print("Greatest Decrease in Revenue: " + months[min_index] + " ($" + str(Dec_Rev) + ")")


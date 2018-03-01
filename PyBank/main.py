import os
import csv

revenue_data = {} # List to hold the revenues
Total_Revenue = 0 # initialize Total Revenue to Zero
months =[]
revenue = []
Average_Change = 0
reve_diff = []
filepath = input("Enter the file path: ")
filename = input("Enter the file name (include extension): ")

PyBank_csv = os.path.join(filepath, filename)

with open(PyBank_csv, newline="") as csvfile: # open the csv file
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
        reve_diff.append(revenue[i+1]-revenue[i])
    Inc_Rev = int(max(reve_diff))
    Dec_Rev = int(min(reve_diff))
    max_index = int(reve_diff.index(max(reve_diff)))
    min_index = int(reve_diff.index(min(reve_diff)))

# set a variable for output file.
#provide filename for the output file 
output_filename = input("Enter a file name to save the output (with extension. Ex. outputfile.txt) : ")
output_file = os.path.join(filepath, output_filename) 
with open(output_file, 'w', newline ="") as datafile: # creates an output file name in the same folder as the inputfile.
    writer  = csv.writer(datafile)
    writer.writerow(['-----------------------------------------------------------'])
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------------------------------------"])
    # * The total number of months included in the dataset 
    writer.writerow(["Total Months:  "+ str(len(revenue_data))])
    # * The total amount of revenue gained over the entire period
    writer.writerow(["Total Revenue: $" + str(int(sum(revenue_data.values())))])
    # * The average change in revenue between months over the entire period
    writer.writerow(["Average Revenue Change: $" + str(int(Average_Change))])
    # * The greatest increase in revenue (date and amount) over the entire period
    writer.writerow(["Greatest Increase in Revenue: "+ months[max_index+1] + " ($" + str(Inc_Rev) + ")"])
    # * The greatest decrease in revenue (date and amount) over the entire period
    writer.writerow(["Greatest Decrease in Revenue: " + months[min_index+1] + " ($" + str(Dec_Rev) + ")"])
    
with open(output_file, 'r', newline="")as datafile :
    reader = csv.reader(datafile, delimiter = ",")
    for row in reader:
        print(row)


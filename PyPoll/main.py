## Option 2: PyPoll

# You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). 
# Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# * The total number of votes cast
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:
# ```
# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------
# ```
# Your final script must be able to handle any such similarly-structured dataset in the future 
# (i.e you have zero intentions of living in this hillbilly town -- 
#  so your script needs to work without massive re-writes). 
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#import dependencies
import os
import csv

# lists for the voting data
voter_id = []
county = []
voting_data = {}
count = 0
candidates = []
vote_count = [] # to store vote counts for each candidate
# Load and Read each file
file_path = input("Enter the path for the file (without the Filename) : ")
file_name = input("Enter the .csv file name (with file extension) : ")
file = os.path.join(file_path, file_name)
with open(file, newline = "") as csvfile :
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None) # skip header
    for row in csvreader :
        voter_id.append(row[0])
        candidates.append(row[2])
        voting_data[row[0]]=row[2]
# * The total number of votes cast
total_votes = len(voter_id)
# unique candidate values into a new list 'candidates_uni'
candidates_uni = list(set(candidates))
# vote count for each candidate
for i in range (len(candidates_uni)):
    for values in voting_data.values() :
        if values == candidates_uni[i]:
            count += 1
    vote_count.append(count)
    count = 0
max_vote_index = vote_count.index(max(vote_count))


# set a variable for output file.
#provide filename for the output file 
output_filename = input("Enter a file name to save the output (with extension. Ex. outputfile.txt) : ")
output_file = os.path.join(file_path, output_filename) 
with open(output_file, 'w', newline ="") as datafile: # creates an output file name in the same folder as the inputfile.
    writer  = csv.writer(datafile)
    writer.writerow(['-----------------------------------------------------------'])
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------------------------------"])
   # * The total number of votes cast 
    writer.writerow(["Total Votes: " + str(total_votes)])
    writer.writerow(["-------------------------------------------------"])
    # * A complete list of candidates who received votes
    for i in range (len(candidates_uni)):
        writer.writerow([candidates_uni[i] +": "+ str((vote_count[i]/total_votes)*100) +"%  (" + str(vote_count[i]) +")"])
    writer.writerow(["-------------------------------------------------"])
    # * The winner of the election based on popular vote.
    writer.writerow(["Winner: " + str(candidates_uni[max_vote_index])])
    writer.writerow(["-------------------------------------------------"])
    
with open(output_file, 'r', newline="")as datafile :
    reader = csv.reader(datafile, delimiter = ",")
    for row in reader:
        print(row)


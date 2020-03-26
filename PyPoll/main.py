import os
import csv

# "election_data_csv = os.path.join("election_data.csv")"
# election_data_csv = "election_data.csv"


total_votes = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999]
total_net = 0
votecounter = {}
candidates = []



with open("election_data.csv") as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")

    header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1

        if row[2] not in candidates:
            candidates.append(row[2])
            votecounter[row[2]] = 0
        votecounter[row[2]] = votecounter[row[2]] + 1


print(f"Total Votes: {total_votes}")
print(votecounter)

       
import os
import csv

# "budget_data_csv = os.path.join("budget_data.csv")"
# budget_data_csv = "budget_data.csv"


total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999]
total_net = 0



with open("budget_data_file") as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")

    header = next(csvreader)

    first_row = next(csvreader)

    total_months = total_months + 1

    total_net = total_net + int(first_row[1])

    previous_net = int(first_row[1])

    for row in csvreader:
        total_months = total_months + 1

        total_net = total_net + int(row[1])

        net_change = int(row[1]) - previous_net

        previous_net = int(row[1])

        net_change_list = net_change_list + [net_change]

        month_of_change = month_of_change + [row[0]]


        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change 

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change  

net_monthly_average = sum(net_change_list)/len(net_change_list) 

print(f"Total Months: {total_months}")


       
import os
import csv

budget_data.csv = os.path.join("..", "Resources", "budget_data.csv")

def print_total(budget_data):
    date = str(budget_data[0])
    amount = int(budget_data[1])
    profit = int(budget_data[2])
    losses = int(budget_data[3])


'The total number of months included in the dataset'
total_months = date + 

'The net total amount of "Profit/Losses" over the entire period'
total_profit/losses = profit + losses

total_losses = 

'The average of the changes in "Profit/Losses" over the entire period'
total_average = amount/profit + losses

'The greatest increase in profits (date and amount) over the entire period'
total_increase = 

'The greatest decrease in losses (date and amount) over the entire period'


with open(budget_data.csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
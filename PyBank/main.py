import os
import csv

file = csv.reader(open("Resources/budget_data.csv"), delimiter =',')

#number of months
budget = open("Resources/budget_data.csv")
reader = csv.reader(budget, delimiter = ",")
months = len(list(reader)) - 1


#profits
profits = []
date_amount =[]
for line in file:
    profits.append(line[1])
    date_amount.append(line)
profits = profits[1:]
profits = [int(x) for x in profits]
final_profit = sum(profits)

#changes in profits
changes = []
for i in range(len(profits)):
    if i == len(profits) - 1:
        break
    else:
        change = profits[i+1] - profits[i]
        changes.append(change)

#average change in profit
sum(changes)/len(profits)

#highest profit
max_profit = max(changes)

#lowest profit
min_profit = min(changes)


date_amount = date_amount[1:]

max_date = (date_amount[changes.index(max_profit) + 1][0], max_profit)

min_date = (date_amount[changes.index(min_profit) + 1][0], min_profit)

#analysis
financial_analysis = print("Financial Analysis:", '\n'
                            "Total Months:",  months, '\n'
                            "Total:", final_profit, '\n'
                            "Average Change:", sum(changes)/len(profits), '\n'
                            "Greatest Increase:", max_date, '\n'
                            "Greatest Decrease:", min_date)

financial_analysis

file = open('financial.txt', 'w+')
file.write("financial_analysis")
file.close()

budget.close()
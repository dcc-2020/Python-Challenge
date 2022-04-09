import os
import csv
import pandas as pd
import sys

csvpath = os.path.join("budget_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    total_month = 0
    total = 0
    changes = 0
    previous = 1088983
    total_changes = []
    month = []
    for i in csvreader:
        total_month += 1
        total += int(i[1])
        changes = (int(i[1]) - previous)
        total_changes.append(changes)
        previous = int(i[1])
        month.append(i[0])

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_month}')
print(f'Total: ${total}')
print(f'Average Change: ${round(sum(total_changes) / (total_month - 1), 2)}')
print(f'Greatest Increase in Profits: {month[total_changes.index(max(total_changes))]} (${max(total_changes)})')
print(f'Greatest Decrease in Profits: {month[total_changes.index(min(total_changes))]} (${min(total_changes)})')


text_file = open('Financial Analysis.txt', 'w')    
sys.stdout = open('Financial Analysis.txt', "w")

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_month}')
print(f'Total: ${total}')
print(f'Average Change: ${round(sum(total_changes) / (total_month - 1), 2)}')
print(f'Greatest Increase in Profits: {month[total_changes.index(max(total_changes))]} (${max(total_changes)})')
print(f'Greatest Decrease in Profits: {month[total_changes.index(min(total_changes))]} (${min(total_changes)})')


text_file.close()
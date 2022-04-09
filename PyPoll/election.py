import os
import csv
import pandas as pd
import sys
from collections import Counter

csvpath = os.path.join("election_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    candidate = []
    result = Counter()

    for i in csvreader:
        if i[2] not in candidate:
            candidate.append(i[2])
        for j in candidate:
            result[j] += i.count(j)

    votes = list(result.values())
    charles = "{:.3%}".format(result["Charles Casper Stockham"] / sum(votes))
    diana = "{:.3%}".format(result["Diana DeGette"] / sum(votes))
    raymon = "{:.3%}".format(result["Raymon Anthony Doane"] / sum(votes))
    

print('Election Results\n-------------------------')
print(f'Total Votes: {sum(votes)}\n-------------------------')
print(f'{candidate[0]}: {charles} ({result["Charles Casper Stockham"]})')
print(f'{candidate[1]}: {diana} ({result["Diana DeGette"]})')
print(f'{candidate[2]}: {raymon} ({result["Raymon Anthony Doane"]})')
print('-------------------------')
print(f'Winner: {max(result, key=result.get)}')
print('-------------------------')


text_file = open('Election Results.txt', 'w')    
sys.stdout = open('Election Results.txt', 'w')

print('Election Results')
print('-------------------------')
print(f'Total Votes: {sum(votes)}')
print('-------------------------')
print(f'{candidate[0]}: {charles} ({result["Charles Casper Stockham"]})')
print(f'{candidate[1]}: {diana} ({result["Diana DeGette"]})')
print(f'{candidate[2]}: {raymon} ({result["Raymon Anthony Doane"]})')
print('-------------------------')
print(f'Winner: {max(result, key=result.get)}')
print('-------------------------')

text_file.close()
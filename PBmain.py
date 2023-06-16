import os
import csv

budget_path = os.path.join('PyBank','Resources', 'budget_data.csv')

with open(budget_path) as budget_file, open(budget_path) as budget_noheader:
    budget_reader = csv.reader(budget_noheader, delimiter = ",")
    print (budget_reader)

print("Financial Analysis")
print("___________________")

first_month = 1

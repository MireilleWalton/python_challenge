import os
import csv

budget_path = os.path.join('PyBank','Resources', 'budget_data.csv')

date = []
amount = []

with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter = ",")
    print (budget_reader)
    budget_data = next(budget_reader)
    print(f"Budget Header: {budget_data}")
    for data_row in budget_reader:
        date.append(data_row [0])
        amount.append(float(data_row[1]))
    print (date)

#how many months?
unique_dates = set (date)
total_dates = len(unique_dates)
print (total_dates)

#sum total amount 

Total_amount = sum(amount)
print (Total_amount)

#here we go looping again - remember corrections from VBA!!!

Ttl_chg_amnt = []
init_amnt = amount[0]
chg_count = 0
max_inc = 0
max_dec = 0

for amnt in amount[1:]: #remember we have a headerow at index row 0 so start is from index row 1)
    chg_amnt = amnt - init_amnt
    Ttl_chg_amnt.append(chg_amnt)
    chg_count += chg_amnt
    init_amt = chg_amnt


#print("Financial Analysis")
#print("___________________")



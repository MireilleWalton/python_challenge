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
    #print (date)

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
Sum_Ttl_chg_amnt = 0
init_amnt = amount[0]
Ttl_chg_count = enumerate(Ttl_chg_amnt)

for amnt in amount[1:]:
    chg_amnt = amnt - init_amnt
    Sum_Ttl_chg_amnt += chg_amnt
    init_amnt = amnt

Avg_chg_amount = Sum_Ttl_chg_amnt / (total_dates - 1)    
print (Avg_chg_amount)

#find greatest inrease and decrease

max_date = max(date)
max_date_index = date.index(max_date)

print (max_date)
print (max_date_index)

#print("Financial Analysis")
#print("___________________")



import os
import csv
import locale

locale.setlocale(locale.LC_ALL, 'en_AU')    #  import local currency, elPastor, 12 March 2017 and S.Lott 26 November 2006 

budget_path = os.path.join('Resources', 'budget_data.csv')   # import data file 

date = []           #   establish list to store dates
amount = []         #   establish list to stora amounts
Ttl_chg_amnt = []   #   establish to store rate of change

with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter = ",")
    print (budget_reader)
    budget_data = next(budget_reader)       #   store budget header
    for data_row in budget_reader:
        date.append(data_row [0])           #   append date data to date list
        amount.append(float(data_row[1]))   #   append amount data to date list
 

Total_dates = len(date)     #   count how many months. Code ref Ulhaq M, 2022 & Bastin N 2010, StackOverflow
Total_amount = sum(amount)  #   calculate total amount 
Sum_Ttl_chg_amnt = 0        #   calculate total amount 
init_amnt = amount[0]
for amnt in amount[1:]:
    chg_amnt = amnt - init_amnt
    Sum_Ttl_chg_amnt += chg_amnt
    init_amnt = amnt

Avg_chg_amount = Sum_Ttl_chg_amnt / (Total_dates - 1)    #   calculate the average amount

Sum_Ttl_chg_amount = 0      #   find greatest inrease and decrease - remember VBA code and get it right! Love the simplified '+=' of python
init_amount = [0]           
max_inc = 0                 
max_inc_date = ""           #   establish respository to store max increase date
min_inc = 0
min_inc_date = ""           #   establish respository to store min increase date

for i in range(1, len(amount)):
    chg_amnt = amount[i] - init_amnt
    Sum_Ttl_chg_amnt += chg_amnt        #  ref; Programming with Mosh
    init_amnt = amount[i]
    if chg_amnt > max_inc:
        max_inc = chg_amnt
        max_inc_date = date[i]
    elif chg_amnt < min_inc:
        min_inc = chg_amnt
        min_inc_date= date[i]

# #   print to terminal.  currency code ref: PythonLab 2022 

print ("Financial Analysis")
print("-------------------------------------")
print (f"Total months:  {Total_dates}")
print ("Total: ${:.0f}" .format(Total_amount))
print ("Average change:  ${:.2f}" .format(Avg_chg_amount))
print ("Greatest increase in profits:  " + (max_inc_date) + "  (${:.0f})" .format(max_inc))
print ("Greatest decrease in profits:  " + (min_inc_date) + "  (${:.0f})" .format(min_inc))
print("-------------------------------------")

#   export results to .txt file.  code ref: Christiansen, A, 2016, StackOverflow

with open(os.path.join('PyBank_main_print_results.txt'), 'w') as f:

    print ("Financial Analysis", file=f)
    print("-------------------------------------", file=f)
    print (f"Total months:  {Total_dates}", file=f)
    print ("Total: ${:.0f}" .format(Total_amount), file=f)
    print ("Average change:  ${:.2f}" .format(Avg_chg_amount), file=f)
    print ("Greatest increase in profits:  " + (max_inc_date) + "  (${:.0f})" .format(max_inc), file=f)
    print ("Greatest decrease in profits:  " + (min_inc_date) + "  (${:.0f})" .format(min_inc), file=f)
    print("-------------------------------------", file=f)


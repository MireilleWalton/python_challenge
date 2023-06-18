import os
import csv
import locale

locale.setlocale(locale.LC_ALL, 'en_AU') # code ref: elPastor, 12 March 2017 and S.Lott 26 November 2006 

election_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')

vote = []
candidates = []

with open(election_path) as election_file:
    election_reader = csv.reader(election_file, delimiter = ",")
    print (election_reader)
    election_data = next(election_reader) #store election header
    #print(f"election Header: {election_data}")  #print election header
    for data_row in election_reader:
        vote.append(data_row [0])
        candidates.append(str(data_row[2]))
    #print (date)

#how many votes? 
vote = set (vote)
total_votes = len(vote) # code ref Ulhaq M, 2022 & Bastin N 2010, StackOverflow
print (total_votes)

#candidate vote count - i want to store it in a dictionary
candidate_pctg = {}
for candidate in candidates:
    if candidate in candidate_pctg:
        (candidate_pctg[candidate]/total_votes)*100
    else:
        percentage = 0

#candidate vote % - i want to store it in a dictionary
candidate_votes = {}
for candidate in candidates:
    if candidate in candidate_votes:
        candidate_votes[candidate] +=1
    else:
        candidate_votes[candidate] = 1

print (candidate_pctg)
print(candidate_votes)


# #     print("Election Results")
# #     print("------------------------")
# #     print(f"Total votes:  {Ttl_votes}")
# #     print("------------------------")
# #     print(f"Sick Time Usage Rate: {str(sick_hours_rate)}")
# #     print(f"Voting Time Usage Rate: {str(voting_time_usage_rate)}")
# #     print(f"Overall Time Off Usage: {str(overall_usage_rate)}")
# #     print(f"{message}")
# #     print("------------------------")
# #     print(f"Winner:)
# #     print("------------------------")

# # Read in the CSV file
# with open(election_csv, 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     header = next(csvreader)

# #   print out profile - loop through rows
#     for row in csvreader:

#   If the candidate votes are greater than 0, run the 'print_profile()' function
    #if election_id_to_check == row[0]:
#             print_profile(row)

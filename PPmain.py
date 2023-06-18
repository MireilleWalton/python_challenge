import os
import csv
import locale

locale.setlocale(locale.LC_ALL, 'en_AU')

#import data file & establish lists

election_path = os.path.join('PyPoll','Resources', 'election_data.csv')

vote = []
candidate = []

with open(election_path) as election_file:
    election_reader = csv.reader(election_file, delimiter = ",")
    print (election_reader)
    election_data = next(election_reader) #store election header
    #print(f"election Header: {election_data}")  #print election header
    for data_row in election_reader:
        vote.append(data_row [0])
        candidate.append(str(data_row[2]))
    #print (vote)

#how many votes?
nmbr_votes = set (vote)
votes = len(nmbr_votes) 

#def print_candidate_profile (election_results):

#how many votes per candidate?
no_cndt_votes = set (candidate)
cndt_votes = len(no_cndt_votes) 
print (candidate + int(cndt_votes))

#sum total candidate 

# Ttl_chg_count = enumerate(Ttl_chg_amnt) #counts number of changes to be used in average calculation

#here we go looping again - remember corrections from VBA_challenge!!!

# Ttl_chg_amnt = [] 
# init_amnt = candidate[0]
# Sum_Ttl_chg_amnt = 0
# init_amnt = candidate[0]
# Ttl_chg_count = enumerate(Ttl_chg_amnt) #counts number of changes to be used in average calculation

# for amnt in candidate[1:]:
#     chg_amnt = amnt - init_amnt
#     Sum_Ttl_chg_amnt += chg_amnt
#     init_amnt = amnt

# Avg_chg_candidate = Sum_Ttl_chg_amnt / (total_votes - 1)    
# #print (Avg_chg_candidate)

# #find greatest inrease and decrease - remember VBA code and get it right! Love the simplified '+=' of python

# Sum_Ttl_chg_candidate = 0
# init_candidate = [0]
# max_inc = 0
# max_inc_vote = ""
# min_inc = 0
# min_inc_vote = ""

# for i in range(1, len(candidate)):
#     chg_amnt = candidate[i] - init_amnt
#     Sum_Ttl_chg_amnt += chg_amnt #ref; Programming with Mosh
#     init_amnt = candidate[i]
#     if chg_amnt > max_inc:
#         max_inc = chg_amnt
#         max_inc_vote = vote[i]
#     elif chg_amnt < min_inc:
#         min_inc = chg_amnt
#         min_inc_vote= vote[i]

# #print to terminal.  currency code ref: PythonLab 2022 

# print ("Financial Analysis")
# print("-------------------------------------")
# print (f"Total months:  {total_votes}")
# print ("Total: ${:.0f}" .format(Total_candidate))
# print ("Average change:  ${:.2f}" .format(Avg_chg_candidate))
# print ("Greatest increase in profits:  " + (max_inc_vote) + "  (${:.0f})" .format(max_inc))
# print ("Greatest decrease in profits:  " + (min_inc_vote) + "  (${:.0f})" .format(min_inc))

# #export results to .txt file.  code ref: Christiansen, A, 2016, StackOverflow

# with open(os.path.join('python_challenge', 'PyBank', 'Resources', 'PBmain_Print_Result.txt', 'w')) as f:

#     print ("Financial Analysis", file=f)
#     print("-------------------------------------", file=f)
#     print (f"Total months:  {total_votes}", file=f)
#     print ("Total: ${:.0f}" .format(Total_candidate), file=f)
#     print ("Average change:  ${:.2f}" .format(Avg_chg_candidate), file=f)
#     print ("Greatest increase in profits:  " + (max_inc_vote) + "  (${:.0f})" .format(max_inc), file=f)
#     print ("Greatest decrease in profits:  " + (min_inc_vote) + "  (${:.0f})" .format(min_inc), file=f)




# Ballot_ID = []
# Candidate = []

# with open(election_path) as election_file:
#     election_reader = csv.reader(election_file, delimiter = ",")
#     print (election_reader)
#     election_data = next(election_reader) #store header
#     print(f"Header: {election_data}")  #print budget header
#     for data_row in election_reader:
#         Ballot_ID.append(data_row [0])
#         Candidate.append(str(data_row[2]))


# Ttl_votes = len(Ballot_ID) 
# Candidate_name = Candidate.count
# Candidate_votes = len(Candidate)

# print (Candidate)

# #create function to store data and carry out calculations

# #calculate total votes cast  
# # Total_Votes = len(Ballot_ID)
# # print (Total_Votes)

# Ballot_ID = []
# Candidate = []

# with open(election_path) as election_file:
#     election_reader = csv.reader(election_file, delimiter = ",")
#     print (election_reader)
#     election_data = next(election_reader) #store header
#     print(f"Header: {election_data}")  #print budget header
#     for data_row in election_reader:
#         Ballot_ID.append(data_row [0])
#         Candidate.append(str(data_row[2]))


# Ttl_votes = len(Ballot_ID) 
# Candidate_name = Candidate.count
# Candidate_votes = len(Candidate)

# print (Candidate)

# #create function to store data and carry out calculations




        

# #calculate total votes cast  
# # Total_Votes = len(Ballot_ID)
# # print (Total_Votes)
import os
import csv

#import data file

election_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')


Ballot_ID = []
Candidate = []

with open(election_path) as election_file:
    election_reader = csv.reader(election_file, delimiter = ",")
    print (election_reader)
    election_data = next(election_reader) #store header
    print(f"Header: {election_data}")  #print budget header
    for data_row in election_reader:
        Ballot_ID.append(data_row [0])
        Candidate.append(str(data_row[2]))


Ttl_votes = len(Ballot_ID) 
Candidate_name = Candidate.count
Candidate_votes = len(Candidate)

print (Candidate)

# #create function to store data and carry out calculations

# def print_candidate_profile (profile_data):
#     #count the votes
#         Unique_votes = set (Ballot_ID)
#         total_votes = len(Unique_votes)    
    
#         Candidate_ttl_votes = len(Candidate_votes>0)
#         Candidate_vote_pctg = (Candidate_ttl_votes / Total_votes)*100


#         print (print_candidate_profile (profile_data))
#         print (print_candidate_profile (total_votes))
  


        

# #calculate total votes cast  
# # Total_Votes = len(Ballot_ID)
# # print (Total_Votes)
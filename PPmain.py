import os
import csv

#import data file

poll_path_csv = os.path.join('PyPoll','Resources', 'election_data.csv')

with open(poll_path_csv) as poll_file:
    poll_reader = csv.reader(poll_file, delimiter = ",")
    poll_data_header = next(poll_reader) #store header
    #print(f"Poll Data Header: {poll_data_header}")

# #create function to store data and carry out calculations

def print_candidate_profile (profile_data):
    Ballot_ID = [str(profile_data[0])]
    County = [str(profile_data[1])]  #data not required?
    Candidate = [str(profile_data[2])]
    Total_votes = len(Ballot_ID) 
    Candidate_votes = len(Candidate)
    Candidate_ttl_votes = len(Candidate_votes>0)
    Candidate_vote_pctg = (Candidate_ttl_votes / Total_votes)*100

    print (print_candidate_profile (profile_data))
    print (print_candidate_profile (Total_votes))
  


        

#calculate total votes cast  
# Total_Votes = len(Ballot_ID)
# print (Total_Votes)
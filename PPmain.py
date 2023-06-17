import os
import csv

poll_path = os.path.join('PyPoll','Resources', 'election_data.csv')

#create empty lists to store data


with open(poll_path) as poll_file:
    poll_reader = csv.reader(poll_file, delimiter = ",")
    print (poll_reader)
    poll_data_header = next(poll_reader) #store header
    print(f"Poll Data Header: {poll_data_header}")
    
    Ballot_ID = []
    County = []
    Candidate = []
    
    for poll_row in poll_reader:
        Ballot_ID.append(poll_data_header [0])
        County.append(poll_data_header [1])
        Candidate.append((poll_data_header [2]))
        

#calculate total votes cast  
Total_Votes = len(Ballot_ID)
print (Total_Votes)
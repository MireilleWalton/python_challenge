import os
import csv
import locale

locale.setlocale(locale.LC_ALL, 'en_AU')

#import data file & establish lists

election_path = os.path.join('PyPoll','Resources', 'election_data.csv')

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
    #print (vote)

#how many votes?
nmbr_votes = len (vote)
votes = set(nmbr_votes) 

#count candidate votes
candidate_votes = [candidates.count(name) for name in candidates] 

#candidate percentage of votes
percentage_votes = [(candidate_votes/votes)*100 for votes in candidate_votes]

#need individudal candidante names in a list
candidate_name = [name for name in enumerate(candidates)]

# I think i need a dictionary

def Profile (profile = {"Name":candidate_name, "vote_tally":candidate_votes, "%_votes":percentage_votes})

print(Profile)







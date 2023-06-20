import os
import csv
import locale

locale.setlocale(locale.LC_ALL, 'en_AU') # code ref: elPastor, 12 March 2017 and S.Lott 26 November 2006 

election_path = os.path.join('PyPoll','Resources', 'election_data.csv')

#   Read in the CSV file, split data at ','
with open(election_path, 'r') as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    header = next(election_data)

#   print out profile - loop through rows
    for data in election_data:
     
#   how many votes? 
        votes = (election_data[0])
        candidates = (election_data[2])
    
#  count candidate votes
    ttl_votes = 0
    for a in votes:
        ttl_votes = ttl_votes +1 
        
    #   nmbr_votes = (vote.count)
    #   votes = set(nmbr_votes) 

#  count candidate votes
    candidate_votes = 0
    for b in candidates:
        candidate_votes = candidate_votes +1 
    #   candidate_votes = [candidates.count(name) for name in candidates] 

#   calculate percentage of votes for each candidate 
    pctg_votes = []
    for c in candidates:
        pctg_votes = (candidate_votes/ttl_votes)*100
    #   percentage_votes = [(candidate_votes/votes)*100 for votes in candidate_votes]

#   find the winner - code ref: Datagy 2021
    winner = []
    for c in candidates:
        if c in candidate_votes:
            winner = max(candidate_votes.values())

#   get candidate names and put them in a list
    candidate = []
    for x in candidates:
        if x in candidate_votes:
            candidate = candidate_votes +1


print("Election Results")
print("------------------------")
print(f"Total votes:  {ttl_votes}")
print("------------------------")
print(f"{candidate[0]}, {:.2f} .format{pctg_votes} {:.0f} .format{candidate_votes}")
print(f"{candidate[1]}, {:.2f} .format{cpctg_votes} {:.0f} .format{candidate_votes}")
print(f"{candidate[2]}, {:.2f} .format{pctg_votes} {:.0f} .format{candidate_votes}")
print("------------------------")
print(f"Winner:  {winner[0]}")
print("------------------------")
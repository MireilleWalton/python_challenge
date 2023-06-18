import os
import csv
import locale

locale.setlocale(locale.LC_ALL, 'en_AU')

#   import data file & establish lists

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

#   how many votes?
    nmbr_votes = (vote.count)
    votes = set(nmbr_votes) 

#   count candidate votes
    candidate_votes = [candidates.count(name) for name in candidates] 

#   candidate percentage of votes
    percentage_votes = [(candidate_votes/votes)*100 for votes in candidate_votes]

#   need individudal candidante names in a list
    candidate_name = [name for name in enumerate(candidates)]

#   I think i need a dictionary
    Profile = {"Name":candidate_name, "%_votes" : percentage_votes, "No. votes" : candidate_votes}

#   identify the winner

    most_votes = max(Profile, key=Profile['No. votes'])
    print(most_votes)

#def Profile (profile = {"Name":candidate_name, "vote_tally":candidate_votes, "%_votes":percentage_votes})


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

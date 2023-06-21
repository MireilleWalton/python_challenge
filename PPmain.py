import os
import csv
import locale

locale.setlocale(locale.LC_ALL, 'en_AU') # code ref: elPastor, 12 March 2017 and S.Lott 26 November 2006 

election_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')

vote = []               #  create a list to store total votes
candidates = []         #  create a list to store candidate names
candidate_votes = {}    #  create a dictionary to store total candidate votes
ttl_votes = 0           #  create a counter to count votes
max_vote = 0            #  create a counter to count max votes
winner = ""             #  create a repository to store name of winner
vt_profile = {}         #  create a repository to store name of idividual candidate votes
pctg_profile ={}        #  create a repository to store name of idividual candidate % of votes

with open(election_path) as election_file:
    election_reader = csv.reader(election_file, delimiter = ",")
    print (election_reader)
    election_data = next(election_reader)   #   store election header
                                           
    for data_row in election_reader:        #   print(f"election Header: {election_data}")  #print election header
        ttl_votes = ttl_votes +1            #   count candidate votes
        candidate = data_row[2]             #   create a list above to store candidate names
        if candidate not in candidates:     #   code Ref: Tutor session with L Hou, 20 June 2023 - ability to include multiple functions in 1 if statement 
            candidates.append(candidate)    #   add candidates to list
            candidate_votes[candidate] = 0  #   start dictionary key value at 0
            vt_profile[candidate] = 0       #   start dictionary key value at 0
            pctg_profile[candidate]= 0      #   start dictionary key value at 0
        candidate_votes[candidate] = candidate_votes[candidate]+1

with open(os.path.join('PyPoll_main_print_results.txt'), 'w') as f:
    
    print("Election Results")               
    print("Election Results", file=f)
    print("----------------------------", file=f)
    print("----------------------------")
    print(f"Total votes:   {ttl_votes}", file=f)
    print(f"Total votes:   {ttl_votes}")
    print("----------------------------", file=f) 
    print("----------------------------") 

    for cdt in candidate_votes:     #   deterime number of each candidate's votes as well as percentage of votes and 
        vt = candidate_votes[cdt]   #   vote count for each candidate
        pctg = (vt/ttl_votes)*100   #   % of votes for each candidate            
        if vt > max_vote:           #   determine the candidate with the max votes 
            max_vote=vt
            winner = cdt  
            vt_profile[cdt] = vt
            pctg_profile[cdt]= '{:.3f}'.format(pctg)           
        Output =  f"{cdt}: {pctg:.3f}% ({vt})\n"
        print(Output, end="", file=f) 
        print(Output, end="")   
    print("----------------------------", file=f) 
    print("----------------------------") 
    print("Winner:",  winner, file=f)
    print("Winner:",  winner)
    print("----------------------------", file=f) 
    print("----------------------------") 
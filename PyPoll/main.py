import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
output_path = os.path.join("analysis", "results.txt")
total_votes = 0
candidate_votes = {}
candidate_percentage = {}


with open(csvpath) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    csv_header = next(election_data)

    for row in election_data:
        total_votes = total_votes + 1
        current_candidate = row[2]

        if current_candidate in candidate_votes:
            candidate_votes[current_candidate] += 1
        else:
            candidate_votes[current_candidate] = 1

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percentage = (votes/total_votes)*100
    candidate_percentage[candidate] = percentage

best_candidate = ""
highest_votes = 0

for candidate, votes in candidate_votes.items():
    if votes > highest_votes:
        highest_votes = votes
        best_candidate = candidate
        
with open(output_path, 'w') as outputfile:     
    print("Election Results")       
    outputfile.write("Election Results\n")
    print("-"*20)
    outputfile.write("-"*20 + "\n")
    print(f"Total Votes: {total_votes}")
    outputfile.write(f"Total Votes: {total_votes}\n")
    
    print("-"*20)
    outputfile.write("-"*20 + "\n")

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = (votes/total_votes)*100
        print(f"{candidate} (%{percentage:,.3f}) {votes}")
        outputfile.write(f"{candidate} (%{percentage:,.3f}) {votes}\n")

    
    # print(candidate_votes)
    # outputfile.write(str(candidate_votes))

    # print(candidate_votes.keys())
    # print(candidate_votes.values())
    # print()
    # print(candidate_votes.items())

    print("-"*20)
    outputfile.write("-"*20 + "\n")
    print(f"Winner: {best_candidate} (%{(highest_votes/total_votes)*100:,.3f}\n")
    outputfile.write(f"Winner: {best_candidate} (%{(highest_votes/total_votes)*100:,.3f}\n")
    print("-"*20)
    outputfile.write("-"*20 + "\n")







# candidate_vote = {"Charles Casper Stockham": 23.049% (85213),
# "Diana DeGette": 73.812% (272892),
# "Raymon Anthony Doane": 3.139% (11606)}
# print(candidate_vote)


# #print(f"candidate_votes: )
# print(f"The winning candidate is {best_candidate}")
# print(f"They had this many votes {highest_votes}")
# print(f"Percentage of votes: %{(highest_votes/total_votes)*100:,.3f}")
# print(f"candidate %{(votes/total_votes)*100:,.3f} ({votes})\n")

    
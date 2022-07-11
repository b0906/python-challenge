# print("Hello, World!")
# print("Isn't this groovy?")
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
candidate_votes = {}


with open(csvpath) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    #print(budget_data)
    csv_header = next(election_data)
    # print(f"CSV Header: {csv_header}")

    for row in election_data:
        current_can = row[2]

        if current_can in candidate_votes:
            candidate_votes[current_can] += 1
        else:
            candidate_votes[current_can] = 1

print(candidate_votes)
print(candidate_votes.keys())
print(candidate_votes.values())
print()
print(candidate_votes.items())


best_candidate = ""
highest_votes = 0

for candidate, votes in candidate_votes.items():
    print("CANDIDATE", candidate)
    print("Number of votes", votes)
    if votes > highest_votes:
        highest_votes = votes
        best_candidate = candidate

print("The winning candidate is ", best_candidate)
print("They had this many votes", highest_votes)


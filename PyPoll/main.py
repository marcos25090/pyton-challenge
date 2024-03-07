import csv
import os

# Use a relative path instead of an absolute path
election_data_path = os.path.join("Resources", "election_data.csv")
OUTPUT_FILE_PATH = os.path.join("Analysis", "election_results.txt")
print(os.path.abspath(election_data_path))

total_votes = 0
candidates = []
votes_per_candidate = {}
winner = ""


if os.path.exists(election_data_path):

    with open(election_data_path) as election_file:
        reader = csv.reader(election_file)
        header = next(reader)

        
        for row in reader:
           
            total_votes += 1

            
            candidate = row[2]

           
            if candidate not in candidates:
                candidates.append(candidate)
                votes_per_candidate[candidate] = 0

            
            votes_per_candidate[candidate] += 1

 
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}


winner = max(votes_per_candidate, key=votes_per_candidate.get)


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


with open(OUTPUT_FILE_PATH, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate in candidates:
        output_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

print(f"Election results have been exported to: {OUTPUT_FILE_PATH}")




    
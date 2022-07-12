from operator import and_
import os 
import csv

csv_path = os.path.join("Resources", "election_data.csv")

print("Election Results")

print("-------------------------")

with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    total_votes = sum(1 for row in csv_output)
    print(f"Total Votes: {total_votes}")

print("-------------------------")

with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    ccs_votes = 0
    dd_votes = 0
    rad_votes = 0

    for row in csv_output:

        if row[2] == "Charles Casper Stockham":
            ccs_votes = ccs_votes + 1

        if row[2] == "Diana DeGette":
            dd_votes = dd_votes + 1

        elif row[2] == "Raymon Anthony Doane":
            rad_votes = rad_votes + 1

    ccs_percent = (ccs_votes / int(total_votes)) * 100
    dd_percent = (dd_votes / int(total_votes)) * 100
    rad_percent = (rad_votes / int(total_votes)) * 100
    
    # https://stackoverflow.com/questions/65827728/round-in-python-doesnt-round-when-applied-to-the-variable-but-does-when-appli
    # Below code is inspired by the forum above, retrieved 7/12
    ccs_percent_r = round(float(ccs_percent), 2)
    dd_percent_r = round(float(dd_percent), 2)
    rad_percent_r = round(float(rad_percent), 2)

    print(f"Charles Casper Stockham: {ccs_percent_r}% ({ccs_votes})")
    print(f"Diana DeGette: {dd_percent_r}% ({dd_votes})")
    print(f"Raymon Anthony Doane: {rad_percent_r}% ({rad_votes})")

    print("-------------------------")

    if ccs_votes > dd_votes and ccs_votes > rad_votes:
        winner = "Charles Casper Stockham"

    if dd_votes > ccs_votes and dd_votes > rad_votes:
        winner = "Diana DeGette"

    elif rad_votes > ccs_votes and rad_votes > dd_votes:
        winner = "Raymon Anthony Doane"

    print(f"Winner: {winner}")

    print("-------------------------")



    


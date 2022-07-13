# Import modules
import os
import csv

#Open the CSV file
csv_path = os.path.join("Resources", "budget_data.csv")

# Output formatting
print("Financial Analysis")
print("----------------------------")

# Create the Total Months variable
with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    total_months = sum(1 for row in csv_output)
    print(f"Total Months: {total_months}")


# Create the Total Profit variable
with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    total = 0
    
    for row in csv_output:
        
        if int(row[1]) != 0:
            total = total + int(row[1])

    print(f"Total: ${total}")


# Create our Average Change variables by subtracting each current month's net profit by the last
with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    last_value = 0
    avg_total = 0
    change_value = 0
    inc_profit = 0
    dec_profit = 0
    
    for row in csv_output:

        column_dates = []
        column_dates = row[0]

        column_money = []
        column_money = row[1]

        if last_value != 0:
            change_value = int(column_money) - int(last_value)
            avg_total = change_value + avg_total

        # Declare our Greatest Increase and Decrease
        if change_value > inc_profit:
            inc_profit = change_value
            inc_row = column_dates
        
        if change_value < dec_profit:
            dec_profit = change_value
            dec_row = column_dates

        last_value = int(column_money)

    avg_mean = (avg_total) / (total_months - 1)
    avg_mean_r = round(float(avg_mean), 2)

    print(f"Average Change: ${avg_mean_r}")
    print(f"Greatest Increase in Profits: {inc_row} (${inc_profit})")
    print(f"Greatest Decrease in Profits: {dec_row} (${dec_profit})")

# Re-print all outputs into the .txt file
# https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
# The thread above was extremely helpful in working out the below code (7/12)
with open("analysis.txt", "w") as analysis_text:

    print("Financial Analysis", file = analysis_text)
    print("----------------------------", file = analysis_text)
    print(f"Total Months: {total_months}", file = analysis_text)
    print(f"Total: ${total}", file = analysis_text)
    print(f"Average Change: ${avg_mean_r}", file = analysis_text)
    print(f"Greatest Increase in Profits: {inc_row} (${inc_profit})", file = analysis_text)
    print(f"Greatest Decrease in Profits: {dec_row} (${dec_profit})", file = analysis_text)

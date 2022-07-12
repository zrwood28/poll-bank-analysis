import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")
print("----------------------------")

with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    total_months = sum(1 for row in csv_output)
    print(f"Total Months: {total_months}")


with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    total = 0
    
    for row in csv_output:
        
        if int(row[1]) != 0:
            total = total + int(row[1])

    print(f"Total: ${total}")


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
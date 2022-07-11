import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")

print("----------------------------")

with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    total_rows = sum(1 for row in csv_output)
    print(f"Total Months: {total_rows}")


with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    net_total = 0
    
    for month_total in csv_output:
        
        if int(month_total[1]) != 0:
            net_total = net_total + int(month_total[1])

    print(f"Total: ${net_total}")


with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    print("Average Change: ")


with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    base_increase = 0
    inc_month = str

    for inc_profit in csv_output:

        if int(inc_profit[1]) > base_increase:
            base_increase = int(inc_profit[1])
            inc_month = str(inc_profit[0])

    print(f"Greatest Increase in Profits: {inc_month} (${base_increase})")


with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    base_decrease = 0
    dec_month = str

    for dec_profit in csv_output:

        if int(dec_profit[1]) < base_decrease:
            base_decrease = int(dec_profit[1])
            dec_month = str(dec_profit[0])

    print(f"Greatest Decrease in Profits: {dec_month} (${base_decrease})")




    










    


























import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")

print("----------------------------")

with open(csv_path) as csvfile:

    csv_output = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_output)

    total_rows = sum(1 for row in csv_output)
    print(f"Total Rows: {total_rows}")

    for row in csv_output:
       net_ = 0 
       for i in row:
             sum += sum(int(i))

    print(sum(int(i))) 






















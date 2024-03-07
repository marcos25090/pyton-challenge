import csv
import os


MAINFILE_PATH = os.path.join("Resources","budget_data.csv")
ANALYSIS_FOLDER = "analysis"  # Use all lowercase for the folder name
OUTPUT_FILE_PATH = os.path.join(ANALYSIS_FOLDER, "financial_analysis.txt")

rowcount = 0
total_months = 0
net_total = 0
changes=[]
prev_profits = 0
greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = "" 
greatest_decrease_amount = 0  
prev_profit = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(MAINFILE_PATH) as mainfile:
    
    readr= csv.reader(mainfile)
    header= next(readr)

    print(header)

    for row in readr:
        print(row)

        rowcount = rowcount +1
        print(rowcount)

        current_profit= int(row[1])
        print(type(current_profit))
             
        total_months += 1
        net_total += int(row[1])
         
        print(total_months)
        print(net_total)

        if total_months > 1:
            change= int(row[1]) - int(prev_profits)
            changes.append(change)

            prev_profits = row[1]

            average_change = sum(changes) / (total_months -1 ) if total_months > 1 else 0

            if change > greatest_increase_amount:
                greatest_increase_date = row[0]
                greatest_increase_amount = change

            elif change < greatest_decrease_amount:
                greatest_decrease_date = row[0]
                greatest_decrease_amount = change

       
        prev_profit = row[1]

        print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

with open(OUTPUT_FILE_PATH, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${round(average_change, 2)}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

print(f"Financial analysis results have been exported to: {OUTPUT_FILE_PATH}")


        






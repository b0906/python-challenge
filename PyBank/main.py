# print("Hello, World!")
# print("Isn't this groovy?")
import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
output_path = os.path.join("analysis", "results.txt")
total_month = 0
total_profit_losses = 0
profit_loss_per_month = []
prev = 0
all_months = []


with open(csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    #print(budget_data)
    csv_header = next(budget_data)
    # print(f"CSV Header: {csv_header}")

    for row in budget_data:
        # print(row)
        total_month = total_month + 1 
        total_profit_losses = int(row [1]) + total_profit_losses
        if total_month == 1:
            #[0]
            profit_loss_per_month.append(0)
            prev = int(row[1])
        else:
            current_profit_loss = int(row[1])-prev
            profit_loss_per_month.append(current_profit_loss)
            prev = int(row[1])
        all_months.append(row[0])

with open(output_path, 'w') as outputfile:
    print("Financial Analysis")
    outputfile.write("Financial Analysis\n")
    print("-"*20)
    outputfile.write("-"*20 + "\n")
    print(f"Total Months: {total_month}")
    outputfile.write(f"Total Months: {total_month}\n")
    print(f"Total: ${total_profit_losses:,}")
    outputfile.write(f"Total: ${total_profit_losses:,}\n")
    print(f"Average Change: ${sum(profit_loss_per_month)/(total_month-1):,.2f}")
    outputfile.write(f"Average Change: ${sum(profit_loss_per_month)/(total_month-1):,.2f}\n")

    max_pl = max(profit_loss_per_month)
    index_of_max = profit_loss_per_month.index(max_pl)
    max_month = all_months[index_of_max]
    print(f"Greatest Increase in Profits: {max_month} (${max_pl:,})")
    outputfile.write(f"Greatest Increase in Profits: {max_month} (${max_pl:,})\n")

    min_pl = min(profit_loss_per_month)
    index_of_min = profit_loss_per_month.index(min_pl)
    min_month = all_months[index_of_min]
    print(f"Greatest Decrease in Profits: {min_month} (${min_pl:,})")
    outputfile.write(f"Greatest Decrease in Profits: {min_month} (${min_pl:,})\n")

#import os to allow us to create files and csv for reading csv files

import os
import csv

#define file path for budget_data csv

csvpath = os.path.join("..","Resources","budget_data.csv")

#define and set variables 

date = []
net_profit = []
revenue_changes = []
 
count = 0
total_profit = 0
change_in_profits = 0
starting_profit = 0

#open the CSV using the set path - 03Python - Day 3 - Activity 4

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    #counting the # of rows under date & profit/losses column - https://stackoverflow.com/questions/56607529/looping-through-rows-with-a-column-title & assistnce from vol data dir.
    for row in csvreader:    
      count = count + 1 
      date.append(row[0])

      total_profit = total_profit + int(row[1])
      net_profit.append(row[1])
      
      #calculating the average change in profit on a monthly basis 
      closing_profit = int(row[1])
      monthly_change_in_profits = closing_profit - starting_profit

      #store monthly changes in a list as revenue changes - https://www.programiz.com/python-programming/methods/list/append
      revenue_changes.append(monthly_change_in_profits)
      change_in_profits = change_in_profits + monthly_change_in_profits
      starting_profit = closing_profit

      #calculating the average change in profit
      average_change_profits = (change_in_profits/count)
      
      #finding the greatest and lowest profit/loss & the date it occured
      greatest_increase_profits = max(revenue_changes)
      increase_date = date[revenue_changes.index(greatest_increase_profits)]
      greatest_decrease_profits = min(revenue_changes)
      decrease_date = date[revenue_changes.index(greatest_decrease_profits)]
      
   #print analysis
    print("Financial Analysis")
    print("------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

 # output to a text file - https://stackoverflow.com/questions/34571390/reading-writing-files-in-python
    file = open("Financial Analysis.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("------------------------------------------------" + "\n")
    file.write("Total Months: " + str(count) + "\n")
    file.write("Total Profits: " + "$" + str(total_profit) +"\n")
    file.write("Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    file.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    file.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    file.close()

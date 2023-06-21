#import os to allow us to create files and csv for reading csv files

import os
import csv

#define file path for election_data csv

csvpath = os.path.join("..","Resources","election_data.csv")

#define and set variables 

#variables
votes = []
county = []
candidate = []

#candidates
Charles_Casper_Stockham = []
Charles_Casper_Stockham_Votes = 0
Diana_DeGette = []
Diana_DeGette_Votes = 0
Raymon_Anthony_Doane = []
Raymon_Anthony_Doane_Votes = 0

#open the CSV using the set path

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    #listing the columns of voter id, country, and voted candidate- https://stackoverflow.com/questions/56607529/looping-through-rows-with-a-column-title & assistnce from vol data dir.
    for row in csvreader:     
      votes.append(int(row[0]))
      county.append(row[1])
      candidate.append(row[2])

      #calculate the total count of votes casted
      vote_total = (len(votes))
      
      #calculating votes by person - https://datatofish.com/if-elif-else-python/ & https://www.codecademy.com/resources/docs/python/built-in-functions/len
      for candidate in candidate:
          if candidate == "Charles Casper Stockham":
              Charles_Casper_Stockham.append(candidate)
              Charles_Casper_Stockham_Votes = len(Charles_Casper_Stockham)
              
          elif candidate == "Diana DeGette":
              Diana_DeGette.append(candidate)
              Diana_DeGette_Votes = len(Diana_DeGette)
              
          else: 
              Raymon_Anthony_Doane.append(candidate)
              Raymon_Anthony_Doane_Votes = len(Raymon_Anthony_Doane)
      
      #convert votes into percentages, round to the thousands place
      Charles_Casper_Stockham_Percentage = round(((Charles_Casper_Stockham_Votes /vote_total)*100),3)
      Diana_DeGette_Percentage = round(((Diana_DeGette_Votes /vote_total)*100),3)
      Raymon_Anthony_Doane_Percentage = round(((Raymon_Anthony_Doane_Votes /vote_total)*100),3)

      #declare the winner 
      if Charles_Casper_Stockham_Percentage > max(Diana_DeGette_Percentage, Raymon_Anthony_Doane_Percentage):
        winner = "Charles_Casper_Stockham"
      elif Diana_DeGette_Percentage > max(Charles_Casper_Stockham_Percentage, Raymon_Anthony_Doane_Percentage):
        winner = "Diana_DeGette"  
      else:
        winner = "Raymon_Anthony_Doane"
      
   #print analysis
    print("Election Results")
    print("------------------------------------------------")
    print("Total Votes: " + str(vote_total))
    print("------------------------------------------------")
    print("Charles Casper Stockham: " + str(Charles_Casper_Stockham_Percentage) + "%" + str(Charles_Casper_Stockham_Votes))
    print("Diana DeGette: " + str(Diana_DeGette_Percentage) + "%" + str(Diana_DeGette_Votes))
    print("Raymon Anthony Doane: " + str(Raymon_Anthony_Doane_Percentage) + "%" + str(Raymon_Anthony_Doane_Votes))
    print("------------------------------------------------")
    print("Winner: " + winner) 


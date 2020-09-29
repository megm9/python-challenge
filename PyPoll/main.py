import os
import csv
import pandas as pd


poll = open("Resources/election_data.csv")
reader = csv.reader(poll, delimiter = ",")

#how many votes
reader = csv.reader(poll, delimiter = ",")

votes = len(list(reader)) - 1

poll = open("Resources/election_data.csv")
reader = csv.reader(poll, delimiter = ",")
poll_df = pd.read_csv(poll)

#A complete list of candidates who received votes
Candidate = poll_df['Candidate'].unique()

#The percentage of votes each candidate won

percent = poll_df['Candidate'].value_counts()/votes * 100

#The total number of votes each candidate won

number = poll_df['Candidate'].value_counts()

#The winner of the election based on popular vote

winner = poll_df['Candidate'].value_counts().idxmax()

Election_Results = print("Election Results:", '\n'
                        "Percent of votes:", percent,
                        number, 
                        "Winner is:", winner)

Election_Results 

poll.close()
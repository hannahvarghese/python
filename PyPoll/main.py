import csv

counter = 0
candidate=[]
charlesvote=0
dianavote=0
raymonvote=0
totalvotes=[]
charlespercent=0.0
dianapercent=0.0
raymonpercent=0.0
winner = ""

with open('/Users/hannahvarghese/Documents/python-challenge/PyPoll/Resources/election_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(reader)
    for row in reader:
        candidate+=[row[2]]
        if candidate[counter] == "Charles Casper Stockham":
            charlesvote+=1
        if candidate[counter] == "Diana DeGette": 
            dianavote+=1
        if candidate[counter] == "Raymon Anthony Doane":
            raymonvote+=1
        counter+=1

charlespercent=charlesvote/counter * 100
dianapercent=dianavote/counter * 100
raymonpercent=raymonvote/counter * 100

if charlespercent>dianapercent and raymonpercent:
    winner = "Charles Casper Stockholm"
if dianapercent>charlespercent and raymonpercent:
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"

print ("Election Results")
print ("----------------------")
print ("Total Votes:", counter)
print ("----------------------")
print (f"Charles Casper Stockham : {round(charlespercent, 3)}% ({charlesvote})")
print (f"Diana DeGette           : {round(dianapercent, 3)}% ({dianavote})")
print (f"Raymon Anthony Doane    : {round(raymonpercent, 3)}% ({raymonvote})")
print ("----------------------")
print ("Winner:", winner)
print ("----------------------")
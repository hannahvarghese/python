import csv

counter = 1
nettotal = 1088983
previousprofitloss = 1088983
net_change_list = []
greatestinc=1
greatestdec=1000000000

with open('/Users/hannahvarghese/Documents/python-challenge/PyBank/Resources/budget_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(reader)
    print (header)
    next(reader)
    for row in reader:
        print(row)
        profitloss=int(row[1])
        counter = counter + 1
        nettotal = nettotal + profitloss
        change = profitloss - previousprofitloss
        previousprofitloss = int(row[1])
        net_change_list +=[change]
        if greatestinc<change:
            greatestinc=change
        if greatestdec>change:
            greatestdec=change
    avg_net_change = sum(net_change_list)/len(net_change_list)
     
print ("----------------------")
print ("Financal Analysis")
print ("----------------------")
print ("Total Months:", counter)
print (f"Total: ${nettotal:.2f}\n")
print (f"Average Change: ${avg_net_change:.2f}")
print (f"Greatest Increase in Profits: (${greatestinc})")
print (f"Greatest Decrease in Profits: (${greatestdec})")
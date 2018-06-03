#Jangwon Lee
#Group 8
#Individual HW 4

#1. Answer the question: when using strftime what is the placeholder
#   that will display the month as a 3 letter abbreviation.
#   (ex. "%d" is the placeholder that displays the day as a two digit number)
 
#   -> The answer to this question is #%b


#2.Write an algorithm for step 3.
# 1)open up the file and then read it
# 2)make all data be splited and put them into the list.
# 3)look for the data that is sold on Friday. 
# 4)after finding the data we need, print that out.


#3.Write a program that reads in the information from a file called
#   ShopRecords.csvPreview the documentView in a new window and displays
#   all of the items that were sold on a Friday
#   (hint: use datetime to determine if the date lands on a Friday)

import csv
import datetime

#open up the file
records = csv.DictReader(open("ShopRecords.csv","r"))

#using for loop to find the info
for entry in records:
    #find day month, and year and split them using index position and .split("/")
    D = int(entry["Date"].split("/")[1])
    M = int(entry["Date"].split("/")[0])
    Y = int(entry["Date"].split("/")[2])

    #find the items which were sold on Friday.
    date_time = datetime.date (Y,M,D)
    if date_time.strftime("%A") == "Friday":
        print(entry["Item"])
        

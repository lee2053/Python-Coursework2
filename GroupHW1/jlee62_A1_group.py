#Group Homework 1
#Group 8
#Jangwon Lee & Jessica

import datetime
import csv
#(30 points) Write a function storm_by_event which takes an event type and prints out
# information on all events of that type in Indiana for the year

#1. Strom_by_event

def storm_by_event(event_type):
    #make an empty list to append event,date and county. 
    data = []

    #open the file and read it
    contents = csv.DictReader(open("Indiana_Storms.csv","r"))

    #get information from the excel file

    for item in contents:
        year = item["BEGIN_YEARMONTH"][0:4] 
        month = item["BEGIN_YEARMONTH"][4:] 
        day = item["BEGIN_DAY"]
        
        #get the date when the event happened using index position. 
        finding_date = datetime.date(int(year),int(month),int(day))

        data.append([item["EVENT_TYPE"],
                     finding_date.strftime("%m/%d/%Y"),
                     finding_date.strftime("%A"),
                     finding_date.strftime("%b"),
                     finding_date.strftime("%d"),
                     item["EVENT_NARRATIVE"],
                     item["CZ_NAME"],    
                     item["EPISODE_NARRATIVE"]])
    #formatting the data 
    for section in data:
        if section[0] == event_type:
            print("A", section[0], "happend on", section[1], "in", section[6], "county." + "\n")
                

#(30 points) Write a function storm_by_date which takes a date and prints out
# information on every storm event in Indiana occurring on that date

def storm_by_date(date):
    #make an empty list
    data = []

    #open the file and read it
    contents = csv.DictReader(open("Indiana_Storms.csv","r"))
    
    for item in contents:
        year = item["BEGIN_YEARMONTH"][0:4]
        month = item["BEGIN_YEARMONTH"][4:]
        day = item["BEGIN_DAY"]

        #get the date when the event happened using index position. 
        finding_date = datetime.date(int(year),int(month),int(day))

        data.append([item["EVENT_TYPE"],
                     finding_date.strftime("%m/%d/%Y"),
                     finding_date.strftime("%A"),
                     finding_date.strftime("%b"),
                     finding_date.strftime("%d"),
                     item["EVENT_NARRATIVE"],
                     item["CZ_NAME"],
                     item["EPISODE_NARRATIVE"]])
    for section in data:
        if section[1] == date.strftime("%m/%d/%Y"):
            print("A", section[0], "happend on", section[1], "in", section[6], "county." + "\n")
                

#(Bonus +10) Narrative events: Alter the format of your output so that it includes full descriptions of each event, nicely formatted. 
        
def episode_event(event_type):
    data = csv.DictReader(open("Indiana_Storms.csv","r"))
    for entry in data:
        if entry["EVENT_TYPE"] == event_type and entry["EVENT_NARRATIVE"] != "":
            print("\n",entry["EPISODE_NARRATIVE"],"This was reported in " +entry["CZ_NAME"].title()+" county." + entry["EVENT_NARRATIVE"] + "\n")

def episode_date(date):
    storms = csv.DictReader(open("Indiana_Storms.csv", "r"))
    for entry in storms:
        entry_date_list = entry["BEGIN_DATE_TIME"][:-5].split("/")
        entry_date = datetime.date(int(entry_date_list[2]), int(entry_date_list[0]), int(entry_date_list[1]))
        if entry_date == date and entry["EVENT_NARRATIVE"] != "":
            print("\n"+ date.strftime("On %A the %d of %b ") +entry["EPISODE_NARRATIVE"]+"This was reported in "+entry["CZ_NAME"].title()+" county."+entry["EVENT_NARRATIVE"]+"\n")


#(40 points) Dynamic interaction: Modify your code so that the user is asked
#if they would like to search by date or by event, making sure you get a valid answer.
#If they choose to search by date, ask them for a date and show the events happening on that date.
#If they select event show the events of that type.
while True:
    search = ["date", "event"]
    #make the user enters date or event
    date_event = input("Would you like to search by date or by event? ")

    if date_event.lower() in search:
        #if the user enters event, ask the event what the user looks for
        if date_event == "event":
            date_event = input ("Please enter the type of weather you are searching for: ")
            #print the events out
            storm_by_event(date_event.title())
            episode_event(date_event)
            break
        else:
            #if the user enters the "date", let him enter the exact date again.
            #and print the events on the date when the user wants to look for
            date_input = input("Please enter your date in YYYY/MM/DD format: ")
            date = date_input.split ("/")
            date = datetime.date(int(date[0],),int(date[1]),int(date[2]))
            storm_by_date(date)
            episode_date(date)
            break
    else:
        print("That is not a valid selection. Please try again")
        
        



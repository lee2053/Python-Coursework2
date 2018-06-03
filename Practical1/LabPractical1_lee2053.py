#Jangwon Lee
#Group 8
#Practical 1

#Section 1

#import url and open and read it
#import re so that we use re.findall function
#import webbroswer so that we open the website through python.
import urllib.request, re , webbrowser

web_page = urllib.request.urlopen("http://www.soic.indiana.edu/undergraduate/courses/index.html")
contents = web_page.read().decode(errors="replace")
web_page.close() #after reading it , close it.

#find courses that include CSCI or INFO
csci_courses = re.findall('(?<=CSCI">).+?(?=</a>)',contents)
info_courses = re.findall('(?<=INFO">).+?(?=</a>)',contents)


print("Parsing: http://www.soic.indiana.edu/undergraduate/courses/index.html\n")

#print CSCI courses out
print("CSCI Undergraduate Courses:")
for item in csci_courses:
    print(item)
#pirnt INFO courses out
print("INFO Undergraduate Courses:")
for item in info_courses:
    print(item)

#Section 2

print("\nParsing: http://www.soic.indiana.edu/undergraduate/courses/index.html")
user_input = str(input("Please enter a word to search for:" )) #make the user to enter a word
user_input = user_input.upper() 

user_csci = [] #make an empty list so that we put courses that the user wants to search for.
user_info = [] 


for item in csci_courses:
    if user_input in item.upper(): #if an input of the user is in the list of CSCI courses, append it to the empty list named user_csci.
        user_csci.append(item)
for item in info_courses:
    if user_input in item.upper(): #if an input of the user is in the list of INFO courses, append it to the empty list named user_info.
        user_info.append(item)

print("\nCSCI Undergraduate Courses that match:")
for item in user_csci:   #print the CSCI courses the user searching for.
    print(item)

print("\nINFO Undergraduate Courses that match:")
for item in user_info: #print the INFO courses the user searching for.
    print(item)
    
#Section 3

course_num = input("\nEnter the name of a course(Ex: I210) to view it, or press ENTER:") #make the user to etner the course number
course_num = course_num.upper() 

for item in csci_courses: #if the input of the user is in the list of CSCI courses, 
    if course_num in item.upper():
        item = "CSCI" #make a variable "CSCI" 
        web_page = "http://www.soic.indiana.edu/undergraduate/courses/index.html?number="+course_num+"&department="+item
        webbrowser.open_new_tab(web_page) #open the website

for item in info_courses: #if the input of the user is in the list of INFO courses,
    if course_num in item.upper():
        item ="INFO" #make a variable "INFO"
        web_page = "http://www.soic.indiana.edu/undergraduate/courses/index.html?number="+course_num+"&department="+item
        webbrowser.open_new_tab(web_page) #open the website



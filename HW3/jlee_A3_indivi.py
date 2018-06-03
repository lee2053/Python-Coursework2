#Individual HW#3
#Jangwon Lee
#Group 8

#1.Answer the question: where can you find the Standard Documentation for Python?
# To find the Standard Documentation for Python,
# 1) press F1 button so that we find the standard Documentation for Python.

#2. Write an algorithm for step 3.
 # 1)We need to import os first to use os. functions
 # 2)Need to make a variable that ask the user enter an input
 # 3)get all contents of a directory
 # 4)if the file name includes draft, it is replaced with final.
 # 5)print this out
 
#3. Write a program that asks the user for a path to a directory,
#   then updates the names of all the files in the directory that contain the word draft to instead say final
#   EX: "term paper (draft).txt" would be renamed "term paper (final).txt"

#4. BONUS (5pts): for any .txt file that your program changes the name of,
#                 have your program add a line of text that states "Edited on "
#                 followed by the current date to the end of the text in the file that it is editing.

import os
#make a variable that takes the user input 
directory = input("Please enter a directory for a path: ")
#make the variable that get the current working directory.
directory = os.getcwd()
#get contents of a directory
data = os.listdir(directory)
#print the list contents of a directory before the name of the file is changed
print(os.listdir(directory))

#Bonus step 1.
#create a variable that shows the current date.
current_date = datetime.date.today()

#To change the name of files if the name includes draft.
for file_name in data:
    if os.path.isfile(file_name): # if item in the current directory is a file,
        if "draft" in file_name: # and the name of the file includes draft
            os.rename(file_name, file_name.replace("draft","final")) #replace it with final.
            #BONUS
            #step 2
            #make a file to have a line of text that states "Edited on" followed by the current date.
            edition = ("Edited on" + eval(current_date))
            
            print(os.listdir(directory)) #print the list contents of a directory.
            



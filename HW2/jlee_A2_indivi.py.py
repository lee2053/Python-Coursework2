#Individual Homework 2
#Jangwon Lee
#group 8


#1. Develop algorithms to solve all reamining steps in this problem.

#1) open a text file names "runners.txt" and read each lines.
#2) check by printing "runners.txt" out how it is formed. 
#3) create an empty dictionary based on data given.
#4) create an empty list to put runners' name in the empty list
#5) create an empty list to put runners' name in the empty list
#6) divide each lines into the list named runners and the list named rank using appened function.
#7) Put data into the dictionary named data so that we print out the names of the top 6 finishers
#7) get runners' names that have two parts using .count that finds " " in each line.
##  If there are more than 2 blanks in each line, it will be added to the list named two_names.
#9) get the first three top runners using if statement.

#2. Use a list comprehension to load the data from a file named “runners.txt”.
#There’s a sample filePreview the documentView in a new window on Canvas with the data shown above.
file_contents = [line.strip() for line in open ("runners.txt", "r")]

# print (file_contents)

#create an empty dictionary and list
data = {}
runners = []
rank = []

#with for loop, put all runners in the empty list.
for items in file_contents:
    runners.append(items.strip(items[-1])) #append runners' name into the list named runners
    rank.append(items[-1]) #append runners' rank into the list named rank

#print(runners)
#print(rank)

#3. Use the information read in from the file to print out the names of the top 6 finishers formatted as shown in the example above.
data = {runners[i]:rank[i] for i in range(len(runners))}
print("In the 2016 100 yard dash the top finishers were: ", "\n")
for name in runners:
    print (name, "\n")

#4. Use a list comprehension to create a list of the names that have two parts to them.
two_names = [name for name in runners if int(name.count(" ")) >= 2 ]
print("The people with a two part name are: " , two_names, "\n")


#5. Use a list comprehension to create a list of the people who finished in the top three positions.

top_three = [rank for rank in data if int(data[rank]) <= 3]
print("The top thress finishers were: " , top_three)








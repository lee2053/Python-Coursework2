#Individual HW 5
#Jangwon Lee
#Group 8

#1. Answer the question: what is the pattern that would match a hex color
#   (Links to an external site.)Links to an external site. code.
# for the pattern that would match a hex color, it begins with "#" symbol.
# the length of hex color value is 3 to 6 and a range of valid letter is A to F.

#2. Write an algorithm for step 3.
# 1)import the url and open and read it.
# 2) make an empty list to put all game results
# 3)set wins and losses 0 so that we count every single 'W' and 'L'
# 4)with re.findall, find certain variable.
# 5)if 'W' or 'L' is in the data, wins or losses will be added by 1 every time we find 'W'
# *for the bonus point
# 7)make an empty list to put game scores.
# 8)using re.findall, get scores only and append it to the empty list
# 9) set difference equals to 0
# 10) with .split, find "-" and get scores and losses
# 11) using absolute function, get difference.

#3. Write a program that looks at the source of http://cgi.soic.indiana.edu/~dpierz/mbball.html (Links to an external site.)Links to an external site. (a copy of the IU men's basketball team record page).
# Use regular expressions to find all the games IU has played in this year and calculate the total number of wins and losses (including exhibition games)

import urllib.request #import the url 
import re

#open the url and read it
web_page = urllib.request.urlopen("http://cgi.soic.indiana.edu/~dpierz/mbball.html")
contents = web_page.read().decode(errors = "replace")
web_page.close()

#set wins and losses equal to 0 so that we add 1 whenever we find the data what we want
wins = 0 
losses = 0

#assign the area where I am looking for the games won and lost.
game_data= re.findall('(?<=div class="schedule_game_results"><div>).+?(?=GAME RECAP)',contents, re.DOTALL)


#using for loop, find the games won or lost
for win_and_lose in game_data:
    if 'W' in win_and_lose: #if W is in the list, add 1 to wins
        wins += 1
    if 'L' in win_and_lose: # if L is in the list, add 1 to losses
        losses += 1

#with for loop, find the every single games and append it to the list named games.
##for item in games:
##    each_game = item[0:9] #using index position, get rid of the useless strings.
##    results.append(each_game) #append it to the list

#print it out.
print("Wins: ",wins)
print("Losses:", losses)

#Bonus


results = [] #make an empty list to put game results

for game in game_data: #using re.findall, find "digits - digits" from the data.
    game_result = re.findall('[\d]+[-][\d]+',game)[0]
    results.append(game_result) #append the data we get to the empty list

difference = 0 # set difference 0.

for i in results:
    score = i.split("-")[0] #using .split, find "-" and get the string before "-" in the list.
    score = int(score) #make a string as an integer
    losses = i.split("-")[1] #same thing as above.
    losses = int(losses)
    difference += abs(score - losses) #with abs, which makes integers as an absolute, get total difference
print("Total Difference:" , difference) #print it out.

#! /usr/bin/env python3


print('Content-type: text/html\n')

#INFO-I211 Group Homework 2
#Group 8
#Jangwon Lee, Jessica Young

import cgi
import MySQLdb

string = "i211u17_lee2053" 			#change username to yours!!!
password = "my+sql=i211u17_lee2053" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)

cursor = db_con.cursor()

form = cgi.FieldStorage()

html = """<!doctype html>
<html>
    <head>
	<meta charset="utf-8">
        	<title>Album Lookup</title>
    </head>
    <body>
        <table border=1 width = '650'>
            <h2>ALL CDs with {0} matching {1} </h2>
            <tr>
            <th>Title</th>
            <th>Artist</th>
            <th>Country</th>
            <th>Company</th>
            <th>Price</th>
            <th>Year</th>
            </tr>
            {contents}
        </table>
    </body>
</html>"""

search_criteria = form.getfirst("field", "Title")
search_value = form.getfirst("search", "USA")

                                
table = ""

try:				#Always surround .execute with a try!
    
        SQL = 'SELECT * FROM CD '
        SQL += 'WHERE ' + str(search_criteria) + "=" +'"' + str(search_value) + '";'

        cursor.execute(SQL)
        results = cursor.fetchall()        
except Exception as e:		#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)

else:				#This runs if there was no error
    for item in results:       #row
        table += "<tr>"
        for entry in item:       #column
            table += "<td>"
            table += str(entry)
            table += "</td>"
        table +="</tr>"  
print(html.format(search_criteria, search_value, contents=table))







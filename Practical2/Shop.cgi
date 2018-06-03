#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb, cgi


    
    
#establish DB connection
string = "i211u17_lee2053" 	#change this to yours
password = "my+sql=i211u17_lee2053"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()
form = cgi.FieldStorage()

html = """
    <!doctype html>
        <html>
        <head><meta charset="utf-8">
        <body>
        <h1>Welcome to the Plant Shop</h1>
        <table border='1' width='80%'>
        <tr><th>PlantID</th>
        <th>CommonName</th>
        <th>BotanicalName</th>
        <th>Price</th>
        <th>&nbsp;</th>
        </tr>
       {contents}
        </table>
        </body>
        </html>
        """


try:				#Always surround .execute with a try!
        SQL = "SELECT * FROM Plants;"
        cursor.execute(SQL)
        results = cursor.fetchall()

except Exception as e:		#Here we handle the error
        print ('<p>Something went wrong with the SQL!</p>')
        print (SQL, "Error:", e)

else:				#This runs if there was no error
        result = ""
        for row in results:
            result += '<tr>'
            for entry in row:
                result += "<td align='center'>"+str(entry)+"</td>"
            result += "<td align='center'><a href='PlantBuy1.cgi?plant="+str(row[0])+"'>Buy</a></td>"
            result += "</tr>"
                
print(html.format(contents = result))

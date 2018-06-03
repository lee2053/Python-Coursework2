#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb
import cgi

form = cgi.FieldStorage()


string = "i211u17_lee2053" 		#change username to yours!!!
password = "my+sql=i211u17_lee2053" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()


html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Plant Buy Display</title>
</head>
<body>
<table border=1 width = '500'>
<h1>Purchases</h1>
<tr><th>Name</th><th>Plant</th><th>Quantity</th><th>Price</th><th>Total</th></tr>
{contents}
</table>
</body>
</html>"""



item = form.getfirst("plant")
buyer = form.getfirst("name")
quantity = form.getfirst("quantity")


try:
    SQL = "INSERT INTO Transactions (Buyer, PlantID, Quantity) VALUES ('" +str(buyer)+"','"+str(item)+"','"+str(quantity)+"');"
    cursor.execute(SQL)
    db_con.commit()

    SQL = "SELECT * FROM Transactions;"
    cursor.execute(SQL)
    results = cursor.fetchall()

except Exception as e:		#Here we handle the error
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)

else:				#This runs if there was no error
    result =""
    for row in results:
        result += '<tr>'
        for entry in row:
            result += "<td align='center'>"+str(entry)+"</td>"
        result += "</tr>"

print(html.format(contents=result))

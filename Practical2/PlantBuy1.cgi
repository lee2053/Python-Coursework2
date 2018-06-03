#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb
import cgi




string = "i211u17_lee2053" 		#change username to yours!!!
password = "my+sql=i211u17_lee2053" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

form = cgi.FieldStorage()

item = form.getfirst("plant")

html ="""
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Plant Buy Form</title></head>
    <body>
    <form action="PlantBuyAction.cgi" method="post">
                <input type="hidden" name="pid" value="1">
                <p>Buyer: <input type="text" name="name" /></p>
                <p>Common Name: {common_name}</p>
                <p>Base Name: {botanical}</p>
                <p>Price: {price}</p>
                <p>Quantity: <input type="text" name="quantity" /></p>
                <button type="submit">Submit</button>
	</form>

    </body>
</html>

"""

#I tried to get plant's name, price and botanical name with select funciton. but
#error occurs. 
try:
    SQL = "SELECT CommonName,BotanicalName,Price FROM Plants WHERE PlantID = " + item +";"
    cursor.execute(SQL)
    results = cursor.fetchall()
#I tried to solve this problem but INTERNAL SERVER ERROR keeps occuring!!!!
#When I enter "SELECT CommonName,BotanicalName,Price FROM Plants WHERE PlantID = " + anynumber +";"
#on Putty, I got correct results of the common name, base name, and price of plants. but since I had Internal server error, I cannot check it out.
#A
except Exception as e:		
        print('<p>Something went wrong with the SQL!</p>')
        print(SQL, "Error:", e)

#with the result, I tried to get comman
else:
    common_name = results[0]
    Botanical = results[1]
    Price = results[2]
       
print(html.format(common_name = common_name, botanical = Botanical, price = Price))


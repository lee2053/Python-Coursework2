#! /usr/bin/env python3
print ('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()


html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System Confirmation</title></head>
    <body>
    <h1>Robot Delivery System Confirmation</h1>
    <p>You have selected to have a {item} delivered by {delivery_method}.</p>
<p>Your total comes to $ {total_cost}</p>
    </body>
</html>"""

item = form.getfirst('delivery','unknown item')

total_cost = eval(form.getfirst('cost','0'))

delivery_method = form.getfirst('delivery_method','drone')

if delivery_method == 'drone':
    total_cost += 10
if delivery_method == 'self driving car':
    total_cost += 20
if delivery_method == 'giant robot':
    total_cost += 1000

print(html.format(delivery_method = delivery_method, total_cost = total_cost, item = item))
    

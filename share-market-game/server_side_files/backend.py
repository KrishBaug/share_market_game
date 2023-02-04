import random
import time
import json
from functions_backend import open_json_file, update_status_value

#Initialize variables
update_time = 600 #600 seconds
current_time = time.time()
count = 0

products = {}

data = open_json_file('products.json', 'r')
products = data['products']
count = 0

while count != 5:

    for product in products:
        print(product)
        new_stock_price = float(update_status_value(product))
        product['stock_price'] = new_stock_price
    
    count += 1

open_json_file('products.json', 'w', data)





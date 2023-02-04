import json

product_data_template = {
   "name": "",
   "stock_price": "",
   "fall_rise_range": [
    "",
    ""
   ]
  }



product_name = input("Name of the prouct : ")
stock_price = input("Initial_stock_price : ")
fall_range = input("Fall range : ")
rise_range = input("Rise_range : ")

with open("products.json", "r") as f:
    file = json.loads(f.read())

file['products'].append(product_data_template)

product_info = file['products'][-1]
product_info['name'] = product_name
product_info['stock_price'] = stock_price
product_info['fall_rise_range'][0] = float(fall_range)
product_info['fall_rise_range'][1] = float(rise_range)

with open("products.json", "w") as f:
    json.dump(file, f , indent=2)


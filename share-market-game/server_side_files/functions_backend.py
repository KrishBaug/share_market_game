import json
import random

def open_json_file(file_name, mode, data_set = []):
    if mode == 'r':
        with open(file_name, mode) as f:
            data = json.loads(f.read())
            return data

    elif mode == 'w':
        with open(file_name, mode) as f:
            json.dump(data_set, f, indent=2)


def find_name(data_set, key_pair, value):
    pass


def update_status_value(data_set):
    stock_price = float(data_set['stock_price'])
    profit = random.choice(['t', 'f'])
    fall = data_set['fall_rise_range'][0]
    rise = data_set['fall_rise_range'][1]
    incerease_or_decrease_number = random.uniform(fall, rise)
    change_in_stock_price = float(stock_price) * incerease_or_decrease_number / 100
    if profit == 't':
        new_stock_price = stock_price + change_in_stock_price
        return round(new_stock_price, 2)

    elif profit == 'f':
        new_stock_price = float(stock_price) - float(change_in_stock_price)
        return round(new_stock_price, 2)
    



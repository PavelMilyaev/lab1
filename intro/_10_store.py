#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_store_data():
    #Получение данных о складе
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }
    
    store = {
        '12345': [{'quantity': 27, 'price': 42}],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }
    
    return goods, store

def calculate_inventory(goods, store):
    #Расчет стоимости товаров на складе
    results = {}
    
    # Лампа
    lamp_code = goods['Лампа']
    lamp_items = store[lamp_code]
    lamp_quantity = lamp_items[0]['quantity']
    lamp_cost = lamp_items[0]['quantity'] * lamp_items[0]['price']
    results['Лампа'] = (lamp_quantity, lamp_cost)
    
    # Стол
    table_code = goods['Стол']
    table_items = store[table_code]
    table_quantity = table_items[0]['quantity'] + table_items[1]['quantity']
    table_cost = (table_items[0]['quantity'] * table_items[0]['price'] + 
                  table_items[1]['quantity'] * table_items[1]['price'])
    results['Стол'] = (table_quantity, table_cost)
    
    # Диван
    sofa_code = goods['Диван']
    sofa_items = store[sofa_code]
    sofa_quantity = sofa_items[0]['quantity'] + sofa_items[1]['quantity']
    sofa_cost = (sofa_items[0]['quantity'] * sofa_items[0]['price'] + 
                 sofa_items[1]['quantity'] * sofa_items[1]['price'])
    results['Диван'] = (sofa_quantity, sofa_cost)
    
    # Стул
    chair_code = goods['Стул']
    chair_items = store[chair_code]
    chair_quantity = (chair_items[0]['quantity'] + chair_items[1]['quantity'] + 
                      chair_items[2]['quantity'])
    chair_cost = (chair_items[0]['quantity'] * chair_items[0]['price'] + 
                  chair_items[1]['quantity'] * chair_items[1]['price'] + 
                  chair_items[2]['quantity'] * chair_items[2]['price'])
    results['Стул'] = (chair_quantity, chair_cost)
    
    return results

def run_store_demo():
    #Демонстрация расчета склада
    goods, store = get_store_data()
    inventory = calculate_inventory(goods, store)
    
    for item, (quantity, cost) in inventory.items():
        print(f'{item} - {quantity} шт, стоимость {cost} руб')
    
    return inventory

if __name__ == "__main__":
    run_store_demo()
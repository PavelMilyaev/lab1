#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_shops_data():
    #Получение данных о магазинах
    shops = {
        'ашан': [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
        'пятерочка': [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
        'магнит': [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
    }
    return shops

def find_min_prices(shops):
    #Поиск минимальных цен
    sweets = {}
    
    for shop_name, products in shops.items():
        for product in products:
            name = product['name']
            price = product['price']
            
            if name not in sweets:
                sweets[name] = []
            
            sweets[name].append({'shop': shop_name, 'price': price})
    
    # Сортируем по цене и оставляем 2 минимальных
    for sweet in sweets:
        sweets[sweet].sort(key=lambda x: x['price'])
        sweets[sweet] = sweets[sweet][:2]
    
    return sweets

def run_shopping_demo():
    #Демонстрация поиска минимальных цен
    shops = get_shops_data()
    min_prices = find_min_prices(shops)
    
    print("Минимальные цены на сладости:")
    for sweet, prices in min_prices.items():
        print(f"{sweet}: {prices[0]['shop']} - {prices[0]['price']} руб, "
              f"{prices[1]['shop']} - {prices[1]['price']} руб")
    
    return min_prices

if __name__ == "__main__":
    run_shopping_demo()
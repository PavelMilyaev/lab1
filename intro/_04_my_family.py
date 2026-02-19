#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def create_family_data():
    #Создание данных о семье
    my_family = ['отец', 'мать', 'сын', 'дочь']
    
    my_family_height = [
        ['отец', 180],
        ['мать', 165],
        ['сын', 175],
        ['дочь', 160]
    ]
    
    return my_family, my_family_height

def calculate_heights(family_data):
    #Вычисление роста семьи
    my_family_height = family_data[1]
    
    father_height = my_family_height[0][1]
    total_height = sum(member[1] for member in my_family_height)
    
    return father_height, total_height

def run_family_demo():
    #Демонстрация работы с данными семьи
    family_data = create_family_data()
    father_height, total_height = calculate_heights(family_data)
    
    print(f"Рост отца - {father_height} см")
    print(f"Общий рост моей семьи - {total_height} см")
    
    return father_height, total_height

if __name__ == "__main__":
    run_family_demo()

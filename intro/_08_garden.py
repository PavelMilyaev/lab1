#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_flowers_data():
    #Получение данных о цветах
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
    return garden, meadow

def analyze_flowers(garden, meadow):
    #Анализ цветов в саду и на лугу
    garden_set = set(garden)
    meadow_set = set(meadow)
    
    all_flowers = garden_set.union(meadow_set)
    common_flowers = garden_set.intersection(meadow_set)
    garden_only = garden_set.difference(meadow_set)
    meadow_only = meadow_set.difference(garden_set)
    
    return all_flowers, common_flowers, garden_only, meadow_only

def run_garden_demo():
    #Демонстрация анализа цветов
    garden, meadow = get_flowers_data()
    all_flowers, common, garden_only, meadow_only = analyze_flowers(garden, meadow)
    
    print("Все виды цветов:", sorted(all_flowers))
    print("Цветы в саду и на лугу:", sorted(common))
    print("Только в саду:", sorted(garden_only))
    print("Только на лугу:", sorted(meadow_only))
    
    return all_flowers, common, garden_only, meadow_only

if __name__ == "__main__":
    run_garden_demo()
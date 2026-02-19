#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_cities_data():
    """Получение данных о городах"""
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }
    return sites

def calculate_distances(sites):
    """Вычисление расстояний между городами"""
    distances = {}
    cities = list(sites.keys())
    
    for i, city1 in enumerate(cities):
        distances[city1] = {}
        for j, city2 in enumerate(cities):
            if i != j:
                x1, y1 = sites[city1]
                x2, y2 = sites[city2]
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distances[city1][city2] = round(distance, 2)
    
    return distances

def run_distance_demo():
    """Демонстрация вычисления расстояний"""
    sites = get_cities_data()
    distances = calculate_distances(sites)
    
    print("Расстояния между городами:")
    for city1 in distances:
        for city2, distance in distances[city1].items():
            print(f"{city1} - {city2}: {distance} км")
    
    return distances

if __name__ == "__main__":
    run_distance_demo()
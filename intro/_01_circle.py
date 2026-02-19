#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_circle_area(radius=42, pi=3.1415926):
    #Вычисление площади круга
    area = pi * radius ** 2
    return round(area, 4)

def is_point_in_circle(point, radius=42):
    #Проверка нахождения точки внутри круга
    distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
    return distance <= radius

def run_circle_demo():
    #Демонстрация работы с кругом
    radius = 42
    point_1 = (23, 34)
    point_2 = (30, 30)
    
    area = calculate_circle_area(radius)
    point1_in = is_point_in_circle(point_1, radius)
    point2_in = is_point_in_circle(point_2, radius)
    
    print(f"Площадь круга радиусом {radius}: {area}")
    print(f"Точка {point_1} в круге: {point1_in}")
    print(f"Точка {point_2} в круге: {point2_in}")
    
    return area, point1_in, point2_in

if __name__ == "__main__":
    run_circle_demo()



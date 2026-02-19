#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# Добавляем текущую директорию в путь для импорта
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Импортируем все модули
from _01_circle import run_circle_demo
from _02_operations import run_operations_demo
from _03_favorite_movies import run_movies_demo
from _04_my_family import run_family_demo
from _05_zoo import run_zoo_demo
from _06_songs_list import run_songs_demo
from _07_secret import run_secret_demo
from _08_garden import run_garden_demo
from _09_shopping import run_shopping_demo
from _10_store import run_store_demo
from _00_distance import run_distance_demo


class Lab01Demo:
    """Класс для демонстрации всех заданий лабораторной работы"""
    
    def __init__(self):
        self.results = {}
    
    def run_all_demos(self):
        """Запуск всех демонстраций"""
        print("ЛАБОРАТОРНАЯ РАБОТА №1 - ДЕМОНСТРАЦИЯ ВСЕХ ЗАДАНИЙ")
        
        # Запускаем все демо-функции
        demos = [
            ("00. Расстояния между городами", run_distance_demo),
            ("01. Площадь круга и проверка точек", run_circle_demo),
            ("02. Математические операции", run_operations_demo),
            ("03. Извлечение фильмов из строки", run_movies_demo),
            ("04. Данные о семье и рост", run_family_demo),
            ("05. Управление зоопарком", run_zoo_demo),
            ("06. Время звучания песен", run_songs_demo),
            ("07. Секретное сообщение", run_secret_demo),
            ("08. Анализ цветов в саду и на лугу", run_garden_demo),
            ("09. Поиск минимальных цен", run_shopping_demo),
            ("10. Расчет стоимости товаров на складе", run_store_demo),
        ]
        
        for name, demo_func in demos:
            print(f"\n{name}")
            try:
                result = demo_func()
                self.results[name] = result
                print("Успешно выполнено")
            except Exception as e:
                print(f"Ошибка: {e}")
                self.results[name] = None
        
        self._show_summary()
    
    def run_specific_demo(self, demo_number):
        """Запуск конкретной демонстрации"""
        demos = {
            '00': ("Расстояния между городами", run_distance_demo),
            '01': ("Площадь круга и проверка точек", run_circle_demo),
            '02': ("Математические операции", run_operations_demo),
            '03': ("Извлечение фильмов из строки", run_movies_demo),
            '04': ("Данные о семье и рост", run_family_demo),
            '05': ("Управление зоопарком", run_zoo_demo),
            '06': ("Время звучания песен", run_songs_demo),
            '07': ("Секретное сообщение", run_secret_demo),
            '08': ("Анализ цветов в саду и на лугу", run_garden_demo),
            '09': ("Поиск минимальных цен", run_shopping_demo),
            '10': ("Расчет стоимости товаров на складе", run_store_demo),
        }
        
        if demo_number in demos:
            name, demo_func = demos[demo_number]
            print(f"\n{name}")
            print("-" * 40)
            return demo_func()
        else:
            print("Неверный номер демонстрации")
            return None
    
    def _show_summary(self):
        """Показать сводку результатов"""
        print("СВОДКА РЕЗУЛЬТАТОВ")
        
        successful = sum(1 for result in self.results.values() if result is not None)
        total = len(self.results)
        
        print(f"Успешно выполнено: {successful}/{total}")
        
        for name, result in self.results.items():
            status = "true" if result is not None else "false"
            print(f"{status} {name}")


def main():
    """Главная функция"""
    demo = Lab01Demo()
    
    if len(sys.argv) > 1:
        # Запуск конкретной демонстрации
        demo_number = sys.argv[1]
        demo.run_specific_demo(demo_number)
    else:
        # Запуск всех демонстраций
        demo.run_all_demos()


if __name__ == "__main__":
    main()
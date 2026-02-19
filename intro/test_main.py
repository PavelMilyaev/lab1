#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Тесты для лабораторной работы №1
Используется pytest для тестирования функциональности всех модулей
"""

import pytest
import sys
import os

# Добавляем текущую директорию в путь для импорта
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Импортируем функции из всех модулей
from _00_distance import calculate_distances, get_cities_data
from _01_circle import calculate_circle_area, is_point_in_circle
from _02_operations import solve_equation
from _03_favorite_movies import extract_movies_by_slices
from _04_my_family import create_family_data, calculate_heights
from _05_zoo import manage_zoo
from _06_songs_list import get_songs_data, calculate_songs_time
from _07_secret import decode_secret, get_secret_message
from _08_garden import analyze_flowers, get_flowers_data
from _09_shopping import find_min_prices, get_shops_data
from _10_store import calculate_inventory, get_store_data


class TestDistance:
    """Тесты для задания 00 - Расстояния между городами"""
    
    def test_get_cities_data(self):
        """Тест получения данных о городах"""
        sites = get_cities_data()
        assert isinstance(sites, dict)
        assert 'Moscow' in sites
        assert 'London' in sites
        assert 'Paris' in sites
    
    def test_calculate_distances(self):
        """Тест вычисления расстояний"""
        sites = get_cities_data()
        distances = calculate_distances(sites)
        
        assert isinstance(distances, dict)
        assert 'Moscow' in distances
        assert 'London' in distances['Moscow']
        assert 'Paris' in distances['Moscow']
        
        # Проверяем, что расстояния положительные
        assert distances['Moscow']['London'] > 0
        assert distances['London']['Paris'] > 0


class TestCircle:
    """Тесты для задания 01 - Площадь круга и точки"""
    
    def test_calculate_circle_area(self):
        """Тест вычисления площади круга"""
        # Площадь круга радиусом 1 с pi=3.14
        area = calculate_circle_area(radius=1, pi=3.14)
        assert area == 3.14
        
        # Площадь круга радиусом 10
        area = calculate_circle_area(radius=10, pi=3.14)
        assert area == 314.0
        
        # Проверка округления
        area = calculate_circle_area(radius=42)
        assert isinstance(area, float)
    
    def test_is_point_in_circle(self):
        """Тест проверки нахождения точки в круге"""
        # Точка в центре
        assert is_point_in_circle((0, 0), radius=10) == True
        
        # Точка на границе
        assert is_point_in_circle((10, 0), radius=10) == True
        
        # Точка за пределами
        assert is_point_in_circle((15, 15), radius=10) == False
        
        # Тестовые точки из задания
        assert is_point_in_circle((23, 34), radius=42) == True
        assert is_point_in_circle((30, 30), radius=42) == False


class TestOperations:
    """Тесты для задания 02 - Математические операции"""
    
    def test_solve_equation(self):
        """Тест решения уравнения"""
        result = solve_equation()
        assert result == 25
        assert isinstance(result, int)


class TestMovies:
    """Тесты для задания 03 - Фильмы"""
    
    def test_extract_movies_by_slices(self):
        """Тест извлечения фильмов срезами"""
        movies_string = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
        movies = extract_movies_by_slices(movies_string)
        
        assert len(movies) == 4
        assert movies[0] == 'Терминатор'
        assert movies[1] == 'Назад в будущее'
        assert movies[2] == 'Пятый элемент'
        assert movies[3] == 'Чужие'
        
        # Проверяем, что нет запятых в результатах
        assert ',' not in movies[0]
        assert ',' not in movies[1]


class TestFamily:
    """Тесты для задания 04 - Семья"""
    
    def test_create_family_data(self):
        """Тест создания данных о семье"""
        family, heights = create_family_data()
        
        assert isinstance(family, list)
        assert isinstance(heights, list)
        assert len(family) == 4
        assert len(heights) == 4
    
    def test_calculate_heights(self):
        """Тест вычисления роста"""
        family_data = create_family_data()
        father_height, total_height = calculate_heights(family_data)
        
        assert isinstance(father_height, int)
        assert isinstance(total_height, int)
        assert father_height > 0
        assert total_height > father_height  # Общий рост больше отцовского


class TestZoo:
    """Тесты для задания 05 - Зоопарк"""
    
    def test_manage_zoo(self):
        """Тест управления зоопарком"""
        zoo, lion_pos, lark_pos = manage_zoo()
        
        assert isinstance(zoo, list)
        assert isinstance(lion_pos, int)
        assert isinstance(lark_pos, int)
        
        # Проверяем, что слон удален
        assert 'elephant' not in zoo
        
        # Проверяем, что медведь добавлен
        assert 'bear' in zoo
        
        # Проверяем, что птицы добавлены
        assert 'rooster' in zoo
        assert 'ostrich' in zoo
        assert 'lark' in zoo
        
        # Позиции должны быть положительными
        assert lion_pos > 0
        assert lark_pos > 0


class TestSongs:
    """Тесты для задания 06 - Песни"""
    
    def test_get_songs_data(self):
        """Тест получения данных о песнях"""
        songs_list, songs_dict = get_songs_data()
        
        assert isinstance(songs_list, list)
        assert isinstance(songs_dict, dict)
        assert len(songs_list) > 0
        assert len(songs_dict) > 0
    
    def test_calculate_songs_time(self):
        """Тест вычисления времени песен"""
        songs_list, songs_dict = get_songs_data()
        total_time_1, total_time_2 = calculate_songs_time(songs_list, songs_dict)
        
        assert isinstance(total_time_1, float)
        assert isinstance(total_time_2, float)
        assert total_time_1 > 0
        assert total_time_2 > 0


class TestSecret:
    """Тесты для задания 07 - Секретное сообщение"""
    
    def test_get_secret_message(self):
        """Тест получения секретного сообщения"""
        secret_message = get_secret_message()
        
        assert isinstance(secret_message, list)
        assert len(secret_message) == 5
        assert all(isinstance(item, str) for item in secret_message)
    
    def test_decode_secret(self):
        """Тест декодирования секретного сообщения"""
        secret_message = get_secret_message()
        decoded = decode_secret(secret_message)
        
        assert isinstance(decoded, str)
        assert len(decoded) > 0


class TestGarden:
    """Тесты для задания 08 - Сад и луг"""
    
    def test_get_flowers_data(self):
        """Тест получения данных о цветах"""
        garden, meadow = get_flowers_data()
        
        assert isinstance(garden, tuple)
        assert isinstance(meadow, tuple)
        assert len(garden) > 0
        assert len(meadow) > 0
    
    def test_analyze_flowers(self):
        """Тест анализа цветов"""
        garden, meadow = get_flowers_data()
        all_flowers, common, garden_only, meadow_only = analyze_flowers(garden, meadow)
        
        assert isinstance(all_flowers, set)
        assert isinstance(common, set)
        assert isinstance(garden_only, set)
        assert isinstance(meadow_only, set)
        
        # Проверяем логику множеств
        assert common.issubset(all_flowers)
        assert garden_only.issubset(all_flowers)
        assert meadow_only.issubset(all_flowers)


class TestShopping:
    """Тесты для задания 09 - Покупки"""
    
    def test_get_shops_data(self):
        """Тест получения данных о магазинах"""
        shops = get_shops_data()
        
        assert isinstance(shops, dict)
        assert 'ашан' in shops
        assert 'пятерочка' in shops
        assert 'магнит' in shops
    
    def test_find_min_prices(self):
        """Тест поиска минимальных цен"""
        shops = get_shops_data()
        min_prices = find_min_prices(shops)
        
        assert isinstance(min_prices, dict)
        assert 'печенье' in min_prices
        assert 'конфеты' in min_prices
        assert 'карамель' in min_prices
        assert 'пирожное' in min_prices
        
        # Проверяем, что для каждого товара 2 магазина
        for sweet, prices in min_prices.items():
            assert len(prices) == 2
            assert prices[0]['price'] <= prices[1]['price']  # Первая цена минимальная


class TestStore:
    """Тесты для задания 10 - Склад"""
    
    def test_get_store_data(self):
        """Тест получения данных о складе"""
        goods, store = get_store_data()
        
        assert isinstance(goods, dict)
        assert isinstance(store, dict)
        assert 'Лампа' in goods
        assert 'Стол' in goods
        assert goods['Лампа'] in store
    
    def test_calculate_inventory(self):
        """Тест расчета инвентаря"""
        goods, store = get_store_data()
        inventory = calculate_inventory(goods, store)
        
        assert isinstance(inventory, dict)
        assert 'Лампа' in inventory
        assert 'Стол' in inventory
        assert 'Диван' in inventory
        assert 'Стул' in inventory
        
        # Проверяем структуру результатов
        for item, (quantity, cost) in inventory.items():
            assert isinstance(quantity, int)
            assert isinstance(cost, (int, float))
            assert quantity > 0
            assert cost > 0


class TestIntegration:
    """Интеграционные тесты"""
    
    def test_all_modules_importable(self):
        """Тест, что все модули могут быть импортированы"""
        modules = [
            '_00_distance', '_01_circle', '_02_operations', '_03_favorite_movies',
            '_04_my_family', '_05_zoo', '_06_songs_list', '_07_secret',
            '_08_garden', '_09_shopping', '_10_store'
        ]
        
        for module_name in modules:
            try:
                module = __import__(module_name)
                assert module is not None
            except ImportError:
                pytest.fail(f"Не удалось импортировать модуль {module_name}")
    
    def test_demo_functions_exist(self):
        """Тест, что все демо-функции существуют"""
        modules = {
            '_00_distance': 'run_distance_demo',
            '_01_circle': 'run_circle_demo',
            '_02_operations': 'run_operations_demo',
            '_03_favorite_movies': 'run_movies_demo',
            '_04_my_family': 'run_family_demo',
            '_05_zoo': 'run_zoo_demo',
            '_06_songs_list': 'run_songs_demo',
            '_07_secret': 'run_secret_demo',
            '_08_garden': 'run_garden_demo',
            '_09_shopping': 'run_shopping_demo',
            '_10_store': 'run_store_demo'
        }
        
        for module_name, function_name in modules.items():
            try:
                module = __import__(module_name)
                function = getattr(module, function_name)
                assert callable(function)
            except (ImportError, AttributeError):
                pytest.fail(f"Функция {function_name} не найдена в модуле {module_name}")


# Дополнительные тесты для проверки граничных случаев
class TestEdgeCases:
    """Тесты граничных случаев"""
    
    def test_circle_edge_cases(self):
        """Граничные случаи для круга"""
        # Точка точно на границе круга
        assert is_point_in_circle((42, 0), radius=42) == True
        assert is_point_in_circle((0, 42), radius=42) == True
        
        # Отрицательные координаты
        assert is_point_in_circle((-23, -34), radius=40) == False
    
    def test_family_edge_cases(self):
        """Граничные случаи для семьи"""
        # Проверяем, что функция работает с пустыми данными
        empty_family = []
        empty_heights = []
        
        # Это вызовет ошибку, но тест проверит обработку ошибок
        with pytest.raises(Exception):
            calculate_heights((empty_family, empty_heights))
    
    def test_zoo_edge_cases(self):
        """Граничные случаи для зоопарка"""
        zoo, lion_pos, lark_pos = manage_zoo()
        
        # Проверяем, что позиции в пределах размера зоопарка
        assert lion_pos <= len(zoo)
        assert lark_pos <= len(zoo)


# Фикстуры для pytest
@pytest.fixture
def sample_cities():
    """Фикстура с тестовыми данными городов"""
    return {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }


@pytest.fixture
def sample_flowers():
    """Фикстура с тестовыми данными цветов"""
    garden = ('ромашка', 'роза', 'одуванчик')
    meadow = ('клевер', 'одуванчик', 'ромашка')
    return garden, meadow


def test_with_fixtures(sample_cities, sample_flowers):
    """Тест с использованием фикстур"""
    # Тест с городами
    distances = calculate_distances(sample_cities)
    assert 'Moscow' in distances
    
    # Тест с цветами
    garden, meadow = sample_flowers
    all_flowers, common, garden_only, meadow_only = analyze_flowers(garden, meadow)
    assert 'ромашка' in common
    assert 'роза' in garden_only
    assert 'клевер' in meadow_only


if __name__ == "__main__":
    # Запуск тестов напрямую (альтернатива pytest)
    print("Запуск тестов лабораторной работы №1")
    print("=" * 50)
    
    # Создаем экземпляры тестов и запускаем основные методы
    test_classes = [
        TestDistance(), TestCircle(), TestOperations(), TestMovies(),
        TestFamily(), TestZoo(), TestSongs(), TestSecret(),
        TestGarden(), TestShopping(), TestStore()
    ]
    
    passed = 0
    failed = 0
    
    for test_class in test_classes:
        class_name = test_class.__class__.__name__
        print(f"\nТестирование {class_name}...")
        
        # Получаем все методы тестирования
        test_methods = [method for method in dir(test_class) 
                       if method.startswith('test_')]
        
        for method_name in test_methods:
            try:
                method = getattr(test_class, method_name)
                method()
                print(f"   {method_name}")
                passed += 1
            except Exception as e:
                print(f"   {method_name}: {e}")
                failed += 1
    
    print(f"\n" + "=" * 50)
    print(f"РЕЗУЛЬТАТ: Пройдено: {passed}, Не пройдено: {failed}")
    print(f"УСПЕШНОСТЬ: {passed/(passed+failed)*100:.1f}%")
    
    if failed == 0:
        print("🎉 Все тесты пройдены успешно!")
    else:
        print(f"⚠️  {failed} тестов не пройдено")
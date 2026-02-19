#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def extract_movies_by_slices(movies_string):
    #Извлечение фильмов с помощью срезов
    first_movie = movies_string[0:10]
    last_movie = movies_string[-15:]
    second_movie = movies_string[12:25]
    second_from_end = movies_string[-22:-17]
    
    return first_movie, last_movie, second_movie, second_from_end

def run_movies_demo():
    #Демонстрация работы со строками фильмов
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    
    movies = extract_movies_by_slices(my_favorite_movies)
    
    print("Извлеченные фильмы:")
    print(f"Первый: {movies[0]}")
    print(f"Последний: {movies[1]}")
    print(f"Второй: {movies[2]}")
    print(f"Второй с конца: {movies[3]}")
    
    return movies

if __name__ == "__main__":
    run_movies_demo()

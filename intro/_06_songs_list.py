#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_songs_data():
    #Получение данных о песнях
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]
    
    violator_songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }
    
    return violator_songs_list, violator_songs_dict

def calculate_songs_time(songs_list, songs_dict):
    #Вычисление времени звучания песен
    # Для списка
    halo_time = songs_list[3][1]
    enjoy_silence_time = songs_list[5][1]
    clean_time = songs_list[8][1]
    total_time_1 = halo_time + enjoy_silence_time + clean_time
    
    # Для словаря
    sweetest_time = songs_dict['Sweetest Perfection']
    policy_time = songs_dict['Policy of Truth']
    blue_dress_time = songs_dict['Blue Dress']
    total_time_2 = sweetest_time + policy_time + blue_dress_time
    
    return total_time_1, total_time_2

def run_songs_demo():
    #Демонстрация работы с данными песен
    songs_list, songs_dict = get_songs_data()
    total_time_1, total_time_2 = calculate_songs_time(songs_list, songs_dict)
    
    print(f'Три песни звучат {total_time_1:.2f} минут')
    print(f'А другие три песни звучат {total_time_2:.2f} минут')
    
    return total_time_1, total_time_2

if __name__ == "__main__":
    run_songs_demo()
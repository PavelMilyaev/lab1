#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def manage_zoo():
    #Управление зоопарком
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    
    # Посадить медведя между львом и кенгуру
    zoo.insert(1, 'bear')
    
    # Добавить птиц
    birds = ['rooster', 'ostrich', 'lark']
    zoo.extend(birds)
    
    # Убрать слона
    zoo.remove('elephant')
    
    # Найти позиции животных
    lion_position = zoo.index('lion') + 1
    lark_position = zoo.index('lark') + 1
    
    return zoo, lion_position, lark_position

def run_zoo_demo():
    #Демонстрация управления зоопарком
    zoo, lion_pos, lark_pos = manage_zoo()
    
    print("Состояние зоопарка:", zoo)
    print(f"Лев сидит в клетке №{lion_pos}")
    print(f"Жаворонок сидит в клетке №{lark_pos}")
    
    return zoo, lion_pos, lark_pos

if __name__ == "__main__":
    run_zoo_demo()
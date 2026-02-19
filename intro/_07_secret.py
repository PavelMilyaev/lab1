#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_secret_message():
    #Получение секретного сообщения
    secret_message = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]
    return secret_message

def decode_secret(secret_message):
    #Декодирование секретного сообщения
    full_message = secret_message[0][3] + ' ' + secret_message[1][9:13] + ' ' + secret_message[2][5:15:2] + ' ' + secret_message[3][12:6:-1] + ' ' + secret_message[4][20:15:-1]
    return full_message

def run_secret_demo():
    #Демонстрация декодирования секретного сообщения
    secret_message = get_secret_message()
    decoded = decode_secret(secret_message)
    
    print("Секретное сообщение:", decoded)
    return decoded

if __name__ == "__main__":
    run_secret_demo()


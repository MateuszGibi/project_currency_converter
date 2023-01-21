from utils.temp_units import *
from utils.speed_units import *
from utils.exchange import *
from utils.clear_screen import *

isRunning = True    # Jeżeli ta wartość ulegnie zmianie na False, program przestanie działać
currency_list = ["pln", "usd", "eur", "chf", "gbp"]     # Lista dostępnych walut to przeliczenia. Wystarczy dodać kod waluty aby rozszerzyć funkcionalność aplikacji.

while isRunning:
    print("Widaj w kalkulatorze :)")
    print("Co chcesz przeliczyc?")
    print("1. Predkosc")
    print("2. Temperature")
    print("3. Walute")
    print("0. Wyjdz")
    print(" ") 
    try:
        input1 = int(input("-> "))
    except:
        print("Podaj poprawną wartość!")
        continue 

    if input1 == 1:
        print("Co chcesz przeliczyc?")
        print("1. km/h na m/s")
        print("2. m/s na km/h")
        print(" ")
        input2 = int(input("-> "))
        
        if input2 == 1:
            kh = int(input("Podaj k/h: "))
            print(f"m/s: {kh_to_ms(kh)}")
        if input2 == 2:
            ms = int(input("Podaj m/s: "))
            print(f"k/h: {ms_to_kh(ms)}")

    elif input1 == 2:
        print("Co chcesz przeliczyc?")
        print("1. Cel na far")
        print("2. Far na cel")
        print(" ")

        input2 = int(input("-> "))

        if input2 == 1:
            cel = int(input("Podaj wartosc w cel: "))
            print("--------------------")
            print(f"| Wartosc w far: {cel_to_far(cel)} |")
            print("--------------------")
        
        if input2 == 2:
            far = int(input("Podaj wartosc w far: "))
            print("--------------------")
            print(f"| Wartosc w far: {far_to_cel(far)} |")
            print("--------------------")
        
    elif input1 == 3:
        print("Jaką walute chcesz przeliczyc?")
        for index, currency in enumerate(currency_list):
            print(f"{index + 1}. {currency}")
        
        input2 = int(input("-> "))
        print(f"Na jaką walute chcesz przeliczyc: {currency_list[input2 -1]}")
        new_currency_list = currency_list.copy()
        new_currency_list.remove(new_currency_list[input2 - 1])
        for index, currency in enumerate(new_currency_list):
            print(f"{index + 1}. {currency}")

        input3 = int(input("-> "))
        print(currency_list)
        print(new_currency_list)
        print(f"Podaj ilosc {currency_list[input2 - 1]} do przeliczenia na {new_currency_list[input3 - 1]}")
        value = int(input("-> "))
        if currency_list[input2 - 1] == "pln": 
            clear_screen()
            new_value = from_pln(value, new_currency_list[input3 - 1])
            print("--------------------")
            print(f"| {currency_list[input2 - 1]}: {value} | {new_currency_list[input3 - 1]}: {new_value} |") 
            print("--------------------")
        
        elif new_currency_list[input3 - 1] == "pln":
            clear_screen()
            new_value = to_pln(value, currency_list[input2 - 1])
            print("--------------------")
            print(f"| {currency_list[input2 - 1]}: {value} | {new_currency_list[input3 - 1]}: {new_value} |") 
            print("--------------------")
        
        else:
            clear_screen()
            new_value = convert(value, currency_list[input2 - 1], new_currency_list[input3 - 1])
            print("--------------------")
            print(f"| {currency_list[input2 - 1]}: {value} | {new_currency_list[input3 - 1]}: {new_value} |") 
            print("--------------------")

    elif input1 == 0:
        print("Pa pa :)")
        isRunning = False
    
    else:
        print("Podaj właściwą wartosc!")
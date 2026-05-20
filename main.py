#консольная версия приложения
#работа с ооп
#работа с файлом

#связка всех модулей(архитектуру соед-я)
from district import District #импортируется класс district
from database import districts as raw_data # данные о районах
import analytics #аналитические функции

# Cоздаю объекты (OOP)
#словарь превращаю в объект класса district
district_objects = [
    District(
        d["name"], #беру значение из словаря
        d["air_quality"],   #получаю данные по ключам
        d["traffic"],
        d["infrastructure"],
        d["population_density"]
    )
    for d in raw_data
]

# FILE REPORT 
def generate_report(): #создание txt файла
    #функиця ген-ет текстовый отчет по всем районам
    #открытие файла в режиме записи 
    # utf 8 для код-ки текста
    # w write mode и файл создается заново 
    # opev для автоматического закрытия
    with open("city_report.txt", "w", encoding="utf-8") as file: 
        file.write("SMART CITY REPORT - ALMATY\n")
        file.write("=" * 40 + "\n\n")

        for d in district_objects: #перебор всех районов 
            file.write(f"District: {d.name}\n")
            file.write(f"Air Quality: {d.air_quality}\n")
            file.write(f"Traffic: {d.traffic}\n")
            file.write(f"Infrastructure: {d.infrastructure}\n")
            file.write(f"Population Density: {d.population_density}\n")
            file.write("-" * 40 + "\n")

    print("\nReport saved to city_report.txt\n")

# SHOW ALL
def show_all():
    print("\nCITY REPORT")
    print("=" * 40)

    for d in district_objects:
        d.show() #метод объекта выз-ся ооп

# MENU - консольное приложение 
def menu():
    while True: #бесконечный цикл до выхода
        print("\nSMART CITY MENU")
        print("1 Show all districts")
        print("2 Best air quality")
        print("3 Most traffic")
        print("4 Best infrastructure")
        print("5 Sort by traffic")
        print("6 Generate city report file")
        print("7 Exit")

        choice = input("Choose: ") #получает выбор пользователя

        # option 1
        if choice == "1":
            show_all()

        # option 2
        elif choice == "2":
            best = analytics.best_air_district() #вызов функции из файла аналитики связка
            print(best["name"] if isinstance(best, dict) else best.name)

        # option 3
        elif choice == "3": #создается список для поиска макс
            values = [d.traffic for d in district_objects]
            idx = values.index(max(values)) #индекс находится 
            print(district_objects[idx].name)

        # option 4
        elif choice == "4":
            values = [d.infrastructure for d in district_objects]
            idx = values.index(max(values))
            print(district_objects[idx].name)

        # option 5
        elif choice == "5":
            sorted_list = sorted(district_objects, key=lambda x: x.traffic)
            #ламбда задает критерии сортировки 
            #сортед воз-ет новый отир-ый список нен меня исходных данных 
            for d in sorted_list:
                print(d.name, d.traffic)

        # option6 new file
        elif choice == "6":
            generate_report()

        # выход
        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


menu()

from district import District
from database import districts as raw_data
import analytics

# Cоздаю объекты (OOP)
district_objects = [
    District(
        d["name"],
        d["air_quality"],
        d["traffic"],
        d["infrastructure"],
        d["population_density"]
    )
    for d in raw_data
]


# =========================================================
# FILE REPORT 
# =========================================================
def generate_report():
    with open("city_report.txt", "w", encoding="utf-8") as file:
        file.write("SMART CITY REPORT - ALMATY\n")
        file.write("=" * 40 + "\n\n")

        for d in district_objects:
            file.write(f"District: {d.name}\n")
            file.write(f"Air Quality: {d.air_quality}\n")
            file.write(f"Traffic: {d.traffic}\n")
            file.write(f"Infrastructure: {d.infrastructure}\n")
            file.write(f"Population Density: {d.population_density}\n")
            file.write("-" * 40 + "\n")

    print("\nReport saved to city_report.txt\n")


# =========================================================
# SHOW ALL
# =========================================================
def show_all():
    print("\nCITY REPORT")
    print("=" * 40)

    for d in district_objects:
        d.show()


# =========================================================
# MENU (FIXED ERRORS)
# =========================================================
def menu():
    while True:
        print("\nSMART CITY MENU")
        print("1 Show all districts")
        print("2 Best air quality")
        print("3 Most traffic")
        print("4 Best infrastructure")
        print("5 Sort by traffic")
        print("6 Generate city report file")
        print("7 Exit")

        choice = input("Choose: ")

        # ---------------- OPTION 1 ----------------
        if choice == "1":
            show_all()

        # ---------------- OPTION 2 ----------------
        elif choice == "2":
            best = analytics.best_air_district()
            print(best["name"] if isinstance(best, dict) else best.name)

        # ---------------- OPTION 3 ----------------
        elif choice == "3":
            values = [d.traffic for d in district_objects]
            idx = values.index(max(values))
            print(district_objects[idx].name)

        # ---------------- OPTION 4 ----------------
        elif choice == "4":
            values = [d.infrastructure for d in district_objects]
            idx = values.index(max(values))
            print(district_objects[idx].name)

        # ---------------- OPTION 5 ----------------
        elif choice == "5":
            sorted_list = sorted(district_objects, key=lambda x: x.traffic)
            for d in sorted_list:
                print(d.name, d.traffic)

        # ---------------- OPTION 6 (NEW FILE) ----------------
        elif choice == "6":
            generate_report()

        # ---------------- EXIT ----------------
        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


menu()
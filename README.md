Smart City Analytics System (Almaty)

Project Overview

This project is a Smart City Analytics System developed to analyze and visualize data about districts of Almaty city.

The system allows comparison of districts based on:
- air quality
- traffic congestion
- infrastructure quality
- population density

The project includes both a console-based application using OOP and a graphical user interface built with Tkinter.

Objectives of the Project

- Apply Object-Oriented Programming (OOP)
- Work with structured data (lists and dictionaries)
- Perform statistical analysis
- Visualize data using graphs
- Build a graphical interface
- Implement filtering and search systems
- Generate output reports in a file

Technologies Used

- Python
- Tkinter
- Matplotlib
- NumPy
- Object-Oriented Programming
- File handling

Project Architecture

The project is divided into multiple modules:

main.py
Console version of the system.
It includes:
- menu-based interaction
- OOP implementation
- analysis of districts
- generation of city_report.txt file

main_gui.py
Graphical user interface.
It includes:
- dashboard system
- search functionality
- filters
- table view
- graphs visualization
- multiple windows

analytics.py
Handles statistical calculations:
- average values
- minimum and maximum values
- analysis using NumPy

database.py
Contains raw dataset of districts:
- name
- air quality
- traffic
- infrastructure
- population density

district.py
Implements Object-Oriented Programming:
- District class
- attributes for each district
- method for displaying information

Object-Oriented Programming

The project uses OOP principles.

Each district is represented as an object of the District class with:
- name
- air quality
- traffic
- infrastructure
- population density

This improves code structure, readability, and reusability.

Features

Console Version:
- display all districts
- find best districts by category
- sorting functionality
- generate report file

GUI Version:
- interactive dashboard
- search system
- filtering system
- table view using TreeView
- graphical visualization using Matplotlib
- multiple windows interface

Data Visualization

The project includes:
- line chart showing trends over years
- bar charts for district comparison
- pie chart for infrastructure distribution

File Output

The system generates a file called city_report.txt.

It contains a structured report of all districts and their values.

How to Run

Console version:
python main.py

GUI version:
python main_gui.py

Key Learning Outcomes

This project demonstrates:
- Object-Oriented Programming
- Modular programming
- Data analysis
- GUI development
- File handling
- Data visualization

Author : Zulfina , Alua , Inkar 2502DS

Student project: Smart City Analytics System
Language: Python
Purpose: University final project
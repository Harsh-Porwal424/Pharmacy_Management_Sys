# Pharmacy Management System ReadMe
This document provides an overview of the Pharmacy Management System code and its functionalities.

## Overview
<img width="846" alt="Screenshot 2024-10-09 at 3 23 28 AM" src="https://github.com/user-attachments/assets/4b1a8ec2-8b49-440c-a70f-8b09e0a1efba">
The Pharmacy Management System is a Python application that helps manage pharmaceutical data. It allows you to add, update, delete, and search for medicine information, including details like reference number, company name, medicine type, and more. The application uses the tkinter library for the graphical user interface (GUI) and MySQL as the database.

## Dependencies
Before running the Pharmacy Management System, you need to ensure that you have the following dependencies installed:

Python (3.x recommended)
tkinter (a standard Python library for GUI)
pymysql (Python library for MySQL database connectivity)

## Running the Application
To run the Pharmacy Management System, follow these steps:

1. Ensure that you have Python and the required dependencies installed.

2. Copy the provided code into a Python script file (e.g., pharmacy_management_system.py).

3. Make sure you have a MySQL server installed and running. Update the database connection details in the code as needed.
```
con = pymysql.connect(host="localhost", user="root", password="Root@1234")
```
4. Create a MySQL database named "pharmaDB" (or use a different name, but update it in the code accordingly).

5. Create the necessary tables in the database by running the SQL queries provided in the code:
```
query = 'use pharmaDB'
query = 'create table pharma(ref int primary key, medName varchar(50))'
query = 'create table medicineInfo(refNo int primary key, cmpName varchar(50), medType varchar(20), medName varchar(50), lotNo varchar(20), isDate date, exDate date, uses varchar(100), sideEff varchar(100), dosage varchar(20), prec varchar(100), price float, quan int)'
```

6. Save your changes and execute the script using Python:
```
python pharmacy_management_system.py
```

7. The Pharmacy Management System GUI should open, allowing you to interact with the application.

## Functionality
### Main Medicine Information:
* Add, update, and delete medicine information.
* Search for medicines by reference number, medicine name, lot number, or uses.

### Medicine Add Department:
* Add new medicines to the system.

### Table View:
* View and manage medicine information in a tabular format.
* Perform operations like updating and deleting medicine entries.

## GUI Layout
The GUI is divided into multiple sections, including frames for medicine information, adding medicine, and displaying data in tabular form. There are buttons for performing various operations and searching for medicine information based on different criteria.

## Important Notes
* The code uses a simple tkinter GUI. For a more sophisticated and user-friendly interface, you may consider using other GUI libraries or frameworks.
* Ensure that you handle database connection errors gracefully and securely in a production environment.
* Feel free to customize, enhance, and adapt the Pharmacy Management System according to your specific requirements and use case.

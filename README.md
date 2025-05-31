# Calendar Application: Project Documentation 

### Sampreeti Atta

## Topic and Description

This project implements a **text-based calendar application** using Python. The application allows users to:

- Add reminders to specific dates  
- View reminders for a specific date   
- Browse reminders by week or month  
- Edit or remove reminders  
- Search reminders using keywords  

The calendar state is saved persistently to a JSON file and is automatically loaded when the application starts. The program is operated entirely through a text-based interface. 

The project is implemented using Python 3.10.12 on Ubuntu 22.04 LTS.  

---

## Solution Principle

The application is built using core Python functionalities and follows modular programming principles. It uses a **dictionary** where each key is a date (`YYYY-MM-DD` format), and the value is a **list of reminders** for that date.

The application:

- Loads existing reminders from a JSON file at startup  
- Offers users an interactive menu with input validation  
- Saves all changes back to the JSON file to maintain persistent state  

User interactions are handled through a **menu-driven interface**, which calls appropriate functions based on user input.

---

## Structure of the Project

The project is structured in a modular way, with each feature encapsulated within a function. This promotes clarity, reuse, and easy debugging.

The main sections of the program include:

- Data loading and saving  
- Reminder management (add, edit, remove, search)  
- Calendar browsing (week and month view)  
- Text-based user interface loop  

---

## Functions and Their Interrelationships

| Function Name                    | Description                                                               |
|----------------------------------|---------------------------------------------------------------------------|
| `load_data()`                    | Loads reminders from a JSON file.                                         |
| `save_data(data)`               | Saves the current reminders to a JSON file.                               |
| `show_todays_reminders()`       | Displays reminders for the current day when the app starts.               |
| `add_reminder()`                | Allows the user to add a reminder to a specific date.                     |
| `edit_reminder()`               | Allows the user to edit an existing reminder on a specific date.          |
| `remove_reminder()`             | Lets the user remove a specific reminder from a date.                     |
| `browse_week()`                 | Displays reminders for 7 consecutive days starting from a given date.     |
| `browse_month()`                | Displays all reminders for a selected month.                              |
| `show_reminders_for_date()`     | Displays all reminders on a user-specified date.                          |
| `search_reminders_by_keyword()` | Searches reminders that match a keyword across all dates.                 |
| `main()`                        | The main menu loop that connects all functions and handles user inputs.   |

---

## Use of External Libraries

The project uses the following **standard Python libraries**, which do not require external installation:

- `json`: For saving/loading reminders to/from a `.json` file  
- `os`: To check file existence  
- `datetime`: For date parsing and formatting  
- `calendar`: For calculating days in a month  

No third-party external libraries are used in this project, making it portable and easy to run in any Python environment.

---

## Division of Responsibilities

All responsibilities, including planning, design, implementation, and testing, were carried out independently by Sampreeti Atta. 

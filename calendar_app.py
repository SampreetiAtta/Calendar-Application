"""Project: Calendar Application
Sampreeti Atta"""

import json
import os
from datetime import datetime, timedelta
import calendar 

DATA_FILE = "calendar_data.json"

def load_data():
    """Loads reminder data from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Error: Could not parse data file. Starting with empty data.")
                return {}
    return {}

def save_data(data):
    """Saves reminder data to a JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_todays_reminders(reminders):
    """Displays reminders for today's date."""
    today = datetime.today().strftime("%Y-%m-%d")
    print(f"\nToday's date: {today}")
    if today in reminders and reminders[today]:
        print("Reminders for today:")
        for idx, reminder in enumerate(reminders[today], 1):
            print(f"  {idx}. {reminder}")
    else:
        print("No reminders for today.")

def add_reminder(reminders):
    """Adds a reminder to a specific date."""
    while True:
        date_str = input("\nEnter date for the reminder (YYYY-MM-DD): ")
        try:
            # Validate date format
            datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    reminder_text = input("Enter the reminder text: ").strip()
    if not reminder_text:
        print("Empty reminder was not added.")
        return

    # Add to the list of reminders for that date
    if date_str not in reminders:
        reminders[date_str] = []
    reminders[date_str].append(reminder_text)
    
    print(f"Reminder added for {date_str}.")

def browse_week(reminders):
    """Displays reminders for a selected week starting from a date."""
    while True:
        start_date_str = input("\nEnter the starting date of the week (YYYY-MM-DD): ")
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    print(f"\nReminders from {start_date_str} to next 6 days:")
    for i in range(7):
        day = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        if day in reminders:
            print(f"{day}:")
            for r in reminders[day]:
                print(f"   - {r}")
        else:
            print(f"{day}: No reminders.")


def browse_month(reminders):
    """Displays reminders for a selected month."""
    while True:
        year_str = input("\nEnter year (e.g., 2025): ")
        month_str = input("Enter month number (1-12): ")
        try:
            year = int(year_str)
            month = int(month_str)
            if 1 <= month <= 12:
                break
            else:
                print("Month must be between 1 and 12.")
        except ValueError:
            print("Please enter numeric values.")

    _, num_days = calendar.monthrange(year, month)
    print(f"\nReminders for {calendar.month_name[month]} {year}:")
    for day in range(1, num_days + 1):
        date_str = f"{year}-{month:02d}-{day:02d}"
        if date_str in reminders:
            print(f"{date_str}:")
            for r in reminders[date_str]:
                print(f"   - {r}")
        else:
            print(f"{date_str}: No reminders.")

def show_reminders_for_date(reminders):
    """Shows reminders for a specific date entered by the user."""
    while True:
        date_str = input("\nEnter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    if date_str in reminders and reminders[date_str]:
        print(f"Reminders for {date_str}:")
        for idx, reminder in enumerate(reminders[date_str], 1):
            print(f"  {idx}. {reminder}")
    else:
        print("No reminders for this date.")

def edit_reminder(reminders):
    """Allows the user to edit a reminder on a specific date."""
    date_str = input("\nEnter the date (YYYY-MM-DD): ")
    if date_str not in reminders or not reminders[date_str]:
        print("No reminders found on that date.")
        return

    print(f"\nReminders for {date_str}:")
    for idx, reminder in enumerate(reminders[date_str], 1):
        print(f"  {idx}. {reminder}")
    
    try:
        choice = int(input("Enter the number of the reminder to edit: "))
        if 1 <= choice <= len(reminders[date_str]):
            new_text = input("Enter the new reminder text: ").strip()
            if new_text:
                reminders[date_str][choice - 1] = new_text
                print("Reminder updated.")
            else:
                print("Empty input. Reminder not changed.")
        else:
            print("Invalid reminder number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_reminder(reminders):
    """Allows the user to remove a reminder on a specific date."""
    date_str = input("\nEnter the date (YYYY-MM-DD): ")
    if date_str not in reminders or not reminders[date_str]:
        print("No reminders found on that date.")
        return

    print(f"\nReminders for {date_str}:")
    for idx, reminder in enumerate(reminders[date_str], 1):
        print(f"  {idx}. {reminder}")

    try:
        choice = int(input("Enter the number of the reminder to delete: "))
        if 1 <= choice <= len(reminders[date_str]):
            removed = reminders[date_str].pop(choice - 1)
            print(f"Removed: {removed}")
            if not reminders[date_str]:
                del reminders[date_str]  # Remove empty date
        else:
            print("Invalid reminder number.")
    except ValueError:
        print("Please enter a valid number.")

def search_reminders_by_keyword(reminders):
    """Searches reminders that contain a specific keyword."""
    keyword = input("\nEnter keyword to search: ").strip().lower()
    if not keyword:
        print("Please enter a non-empty keyword.")
        return

    found = False
    print(f"\nResults for keyword: '{keyword}'")
    for date, reminder_list in reminders.items():
        for idx, reminder in enumerate(reminder_list, 1):
            if keyword in reminder.lower():
                print(f"{date} - {idx}. {reminder}")
                found = True

    if not found:
        print("No reminders matched your keyword.")

def main():
    print("Welcome to the Calendar Reminder App!")
    reminders = load_data()
    show_todays_reminders(reminders)

    while True:
        print("\nMain Menu")
        print("1. Add Reminder")
        print("2. Browse Week")
        print("3. Browse Month")
        print("4. View Reminders for a Specific Date")
        print("5. Edit a Reminder")
        print("6. Delete a Reminder")
        print("7. Search Reminders by Keyword")
        print("8. Exit")

        
        choice = input("Select an option (1-7): ").strip()

        if choice == '1':
            add_reminder(reminders)
            save_data(reminders)
        elif choice == '2':
            browse_week(reminders)
        elif choice == '3':
            browse_month(reminders)
        elif choice == '4':
            show_reminders_for_date(reminders)
        elif choice == '5':
            edit_reminder(reminders)
            save_data(reminders)
        elif choice == '6':
            remove_reminder(reminders)
            save_data(reminders)
        elif choice == '7':
            search_reminders_by_keyword(reminders)
        elif choice == '8':
            print("Saving calendar and exiting...")
            save_data(reminders)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()

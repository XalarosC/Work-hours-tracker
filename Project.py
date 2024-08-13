from datetime import datetime
from colorama import Fore, Style


def add_work_hours_to_file(date, start_time, end_time):
    with open("work_hours.txt", "a") as file:
        file.write(f"{date} {start_time} {end_time}\n")


def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%d/%m")
        return True
    except ValueError:
        return False


def validate_time_format(time_str):
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


from datetime import datetime


def calculate_total_hours(file_path="work_hours.txt"):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            total_hours = 0
            for line in lines:
                _, start_time, end_time = line.split()
                start_datetime = datetime.strptime(start_time, "%H:%M")
                end_datetime = datetime.strptime(end_time, "%H:%M")
                duration = end_datetime - start_datetime
                total_hours += duration.total_seconds() / 3600
            return total_hours
    except FileNotFoundError:
        return 0


def delete_file_contents(file_path="work_hours.txt"):
    with open(file_path, "w") as file:
        file.truncate()
    print("File contents deleted.")


def main():
    while True:
        date = input(
            "Enter date (DD/MM), 'payday' to calculate salary, 'delete' to delete all working hours: "
        )

        if date.lower() == "payday":
            total_hours_worked = calculate_total_hours()
            print(
                f"{Fore.GREEN}Time worked: {total_hours_worked :.2f} Hours{Style.RESET_ALL}"
            )
            print(
                f"{Fore.YELLOW}Salary: {total_hours_worked * 5.1:.2f} Euro{Style.RESET_ALL}"
            )
            break

        if date.lower() == "delete":
            delete_file_contents()
            break


        if not validate_date_format(date):
            print("Invalid date format. Please enter in DD/MM format.")
            continue

        while True:
            start_time = input("Enter start time (HH:MM): ")
            if validate_time_format(start_time):
                break
            else:
                print("Invalid time format. Please enter in HH:MM format.")

        while True:
            end_time = input("Enter end time (HH:MM): ")
            if validate_time_format(end_time):
                break
            else:
                print("Invalid time format. Please enter in HH:MM format.")

        add_work_hours_to_file(date, start_time, end_time)
        print("Work hours added successfully!")
        break


if __name__ == "__main__":
    main()

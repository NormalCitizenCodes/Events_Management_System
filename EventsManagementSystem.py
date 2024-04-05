import datetime

#-==============================-GLOBAL VARIABLES-==============================-

def display_menu():
    print("+---+-------------------------------+")
    print("  # |   EVENT MANAGEMENT SYSTEM     │")
    print("+---+-------------------------------+")
    print("│ 1 │     Display Events            │")
    print("│ 2 │     Book an Event             │")
    print("│ 3 │     Update an Event           │")
    print("│ 4 │     Edit Event Status         │")
    print("│ 5 │     Delete an Event           │")
    print("│ 6 │     Exit                      │")
    print("+---+-------------------------------+")

# -==============================-GLOBAL FOR BOOK EVENT AND SCHEDULES-==============================-
class BookEvent:

    def __init__(self):
        current_date_time = datetime.datetime.now()  # Access the date and time
        self.current_year = int(current_date_time.strftime("%Y"))  # Return current Year
        self.current_month = current_date_time.strftime("%b")  # Return current Month in Abbreviation
        self.current_month_not_abr = current_date_time.strftime("%B")  # Return current Month in not Abbreviation
        self.current_day = int(current_date_time.strftime("%d"))  # Return current Day
        self.current_hour = int(current_date_time.strftime("%H"))  # Return current Hour
        self.current_minute = int(current_date_time.strftime("%M"))  # Return current Minutes
        self.current_second = int(current_date_time.strftime("%S"))  # Return current Seconds
        self.current_midday = current_date_time.strftime("%p")  # Return the current midday (AM or PM)

    def book_event_name(self):

        hour_time = self.current_hour
        if self.current_hour > 12:
            hour_time = self.current_hour - 12

        print("Current Date:", self.current_month, self.current_day, self.current_year)
        print(f"Current Time: {hour_time}:{self.current_minute}:{self.current_second} {self.current_midday}")
        event_name = input("Event name                           : ").strip().title()
        event_venue = input("Event venue                          : ").strip().title()
        return [event_name, event_venue]

    def book_event_year(self):
        while True:
            event_year = input("Enter event year                     : ").strip()
            if event_year.isdigit() and int(event_year) >= self.current_year:
                return int(event_year)
            else:
                print("INVALID: Only current or future years are accepted. Past years and letters are invalid.")

    def book_event_month(self, user_event_year):
        month_abr = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]
        month_not_abr = [
            "January", "February", "March", "April", "May",
            "June", "July", "August", "September", "October",
            "November", "December"
        ]

        while True:
            event_month = input("Enter event month (ex. Dec/December) : ").strip().capitalize()
            if event_month in month_abr or event_month in month_not_abr:
                if user_event_year == self.current_year:
                    if event_month in month_abr and month_abr.index(event_month) >= month_abr.index(self.current_month):
                        return month_abr[month_abr.index(event_month)]
                    elif event_month in month_not_abr and month_not_abr.index(event_month) >= month_abr.index(
                            self.current_month):
                        return month_abr[month_not_abr.index(event_month)]
                    else:
                        print("INVALID: Only current or future months are accepted.")
                else:
                    if event_month in month_abr:
                        return month_abr[month_abr.index(event_month)]
                    elif event_month in month_not_abr:
                        return month_abr[month_not_abr.index(event_month)]
                    else:
                        print("INVALID: Only current or future months are accepted.")
            else:
                print("INCORRECT SPELL: Only numbers no letters or special characters")


    def book_event_day(self, user_event_year, user_event_month):  # This function validate the event day

        month_31_day = [
            "January", "March", "May", "July", "August", "October", "December",
            "Jan", "Mar", "Jul", "Aug", "Oct", "Dec"
        ]

        month_30_day = [
            "April", "June", "September", "November",
            "Apr", "Jun", "Sep", "Nov"
        ]

        month_spec_day = [
            "February", "Feb"
        ]

        while True:
            event_days = input("Enter event day                      : ").strip()

            if event_days.isdigit():

                if (user_event_year == self.current_year and (user_event_month == self.current_month or
                                                              user_event_month == self.current_month_not_abr)):
                    if user_event_month in month_31_day and self.current_day <= int(event_days) <= 31:
                        return event_days
                    elif user_event_month in month_30_day and self.current_day <= int(event_days) <= 30:
                        return event_days
                    elif (user_event_month in month_spec_day and int(user_event_year) % 4 == 0 and
                          self.current_day <= int(event_days) <= 29):
                        return event_days
                    elif (user_event_month in month_spec_day and int(user_event_year) % 4 != 0 and
                          self.current_day <= int(event_days) <= 28):
                        return event_days
                    else:
                        print("INVALID: Only current or future days are accepted. Try Again")
                else:
                    if user_event_month in month_31_day and 0 < int(event_days) <= 31:
                        return event_days
                    elif user_event_month in month_30_day and 0 < int(event_days) <= 30:
                        return event_days
                    elif user_event_month in month_spec_day and int(user_event_year) % 4 == 0 and 0 < int(
                            event_days) <= 29:
                        return event_days
                    elif user_event_month in month_spec_day and int(user_event_year) % 4 != 0 and 0 < int(
                            event_days) <= 28:
                        return event_days
                    else:
                        print("EXCEEDED: Only the days within the month. Try Again.")
            else:
                print("INVALID: Only numbers no letters or special characters")

    def book_event_time(self, user_event_year, user_event_month, user_event_day):
        while True:
            event_time = input("Enter event time (ex. 12:00 AM/PM)   : ").strip().upper()

            try:
                parts = event_time.split()
                if len(parts) != 2:
                    raise ValueError
                time_part = parts[0].split(':')
                if len(time_part) != 2:
                    raise ValueError
                hour, minute = map(int, time_part)
                meantime = parts[1]

                if (0 <= hour < 13 and 0 <= minute < 60 and
                        (meantime == 'AM' or meantime == 'PM')):
                    if (user_event_year == self.current_year and user_event_month == self.current_month and
                            int(user_event_day) == self.current_day):
                        if hour > self.current_hour or (
                                hour == self.current_hour and minute > self.current_minute):
                            return [f"{hour}:{minute:02d}", meantime]
                        else:
                            print("INVALID: Please ensure the time is set at least 1 hour ahead of the current time.")
                    else:
                        return [f"{hour}:{minute:02d}", meantime]
                else:
                    raise ValueError
            except ValueError:
                print("Invalid time format. Please enter time in the format '3:00 AM/PM'.")


event_store = []
event_name_store = []

# -==============================-GLOBAL FOR DISPLAY EVENTS-==============================-
def display_events(events):
    if not events:
        print("No events available.")
    else:
        event_store.sort(key=lambda x: datetime.datetime.strptime(x[2], "%b %d %Y %I:%M %p"))
        print("+---+----------------------------------------+---------------------+---------------------+------------+")
        print("│ # │               EVENT NAME               │      EVENT VENUE    │       SCHEDULE      │   STATUS   │")
        print("+---+----------------------------------------+---------------------+---------------------+------------+")
        for i, event in enumerate(events, 1):
            number = str(i).center(3)
            name = event[0].center(40)
            venue = event[1].center(21)
            schedule = event[2].center(21)
            status = event[3].center(12) if len(event) > 3 else ''.center(12)  # Ensure status is displayed
            print(f"│{number}│{name}│{venue}│{schedule}│{status}│")
        print("+---+----------------------------------------+---------------------+---------------------+------------+")


# -==============================-GLOBAL FOR EVENT STATUS-==============================-
def change_event_status(events, eventStatus):
    try:
        event_num = int(input("Enter the number of the event you want to update: "))
        if 1 <= event_num <= len(events):
            if len(events[event_num - 1]) >= 4:  # Check if the list has enough elements
                choice = input("Type 'C' to cancel or 'A' to activate: ").upper()
                if choice == 'C':
                    events[event_num - 1][3] = eventStatus[1]  # Update event status directly
                elif choice == 'A':
                    events[event_num - 1][3] = eventStatus[0]  # Update event status directly
                else:
                    print("Invalid input")
            else:
                print("Event information does not contain enough elements.")
        else:
            print("Invalid event number")
    except ValueError:
        print("ERROR: Please enter valid input")

# -==============================-GLOBAL VARIABLE FOR DELETE-==============================-
def delete_event(events):
    try:
        event_num = int(input("Enter the number of the event you want to delete: "))
        if 1 <= event_num <= len(events):
            del events[event_num - 1]
            print("Event deleted successfully.")
        else:
            print("Invalid event number")
    except ValueError:
        print("ERROR: Please enter a valid input")


#-==============================-DISPLAY EVENT STATUS-==============================-
while True:
    display_menu()
    user_choose = input("Choose: ")

    if user_choose == "1":
        display_events(event_store)

# -==============================-BOOKS AN EVENT-==============================-
    elif user_choose == "2":
        book_event = BookEvent()
        name_venue = book_event.book_event_name()
        year = book_event.book_event_year()
        month = book_event.book_event_month(year)
        day = book_event.book_event_day(year, month)
        time = book_event.book_event_time(year, month, day)
        formatted_date = month + " " + day + " " + str(year)
        formatted_time = str(time[0]) + " " + str(time[1])
        formatted_event_sche = formatted_date + " " + formatted_time

        if name_venue[0] in event_name_store:
            list_loc = event_name_store.index(name_venue[0]) + 1
            print(f"\033[0;31mThe event name is already been added\033[0m at {list_loc}")
            display_events(event_store)

            while True:
                change_name = input("Change name(Y/N):").strip().upper()
                if change_name == "Y":
                    change_event_name = input("Enter event name: ").strip().title()
                    if change_event_name in event_name_store:
                        print(f"The {change_event_name} as event name is already been stored. Try new event name.")
                    else:
                        name_venue[0] = change_event_name
                        event_info = [name_venue[0], name_venue[1], formatted_event_sche, '']
                        event_store.append(event_info)
                        event_name_store.append(name_venue[0])
                        break
                elif change_name == "N":
                    break
                else:
                    print("Invalid Choice")
        else:
            event_info = [name_venue[0], name_venue[1], formatted_event_sche, 'Active']
            event_store.append(event_info)
            event_store.sort(key=lambda x: datetime.datetime.strptime(x[2], "%b %d %Y %I:%M %p"))
            event_name_store = [name_store[0] for name_store in event_store]

# -==============================-UPDATE AN EVENT-==============================-

    elif user_choose == "3":
        print("+---+----------------------------------------+---------------------+---------------------+------------+")
        print("│ # │               EVENT NAME               │      EVENT VENUE    │       SCHEDULE      │   STATUS   │")
        print("+---+----------------------------------------+---------------------+---------------------+------------+")
        for display_info in range(len(event_store)):
            number = str(display_info + 1).center(3)
            name = event_store[display_info][0].center(40)
            venue = event_store[display_info][1].center(21)
            schedule = event_store[display_info][2].center(21)
            status = event_store[display_info][3].center(12)
            print(f"│{number}│{name}│{venue}│{schedule}│{status}│")
        print("+---+----------------------------------------+---------------------+---------------------+------------+")

        update_loop = True
        while update_loop:
            update_event = input("Enter the number of the event you want to update: ").strip()

            if update_event.isdigit() and 0 < int(update_event) <= len(event_store):
                print("\nEVENT INFORMATION:")
                print("Event name   :", event_store[int(update_event) - 1][0])
                print("Event venue  :", event_store[int(update_event) - 1][1])
                print("Event time   :", event_store[int(update_event) - 1][2])
                print("Event status :", event_store[int(update_event) - 1][3])

                print("+-----+-----------------------+")
                print("│  #  │     Choose Update     │")
                print("+-----+-----------------------+")
                print("│  1  │     Event Name        │")
                print("│  2  │     Event Venue       │")
                print("│  3  │     Event Schedule    │")
                print("+-----+-----------------------+")

                while True:
                    update_choose = input("Choose:").strip()

                    if update_choose == "1":
                        update_event_name = input("Event name: ").strip().title()

                        if update_event_name in event_name_store:
                            print("The event name is already been added. Try again.")
                        else:
                            event_store[int(update_event) - 1][0] = update_event_name
                            event_store.sort(key=lambda x: datetime.datetime.strptime(x[2], "%b %d %Y %I:%M %p"))
                            event_name_store = [name_store[0] for name_store in event_store]
                            update_loop = False
                            break

                    elif update_choose == "2":

                        update_event_venue = input("Event venue: ").strip().title()
                        event_store[int(update_event) - 1][1] = update_event_venue
                        update_loop = False
                        break

                    elif update_choose == "3":

                        update_book_event = BookEvent()
                        year = update_book_event.book_event_year()
                        month = update_book_event.book_event_month(year)
                        day = update_book_event.book_event_day(year, month)
                        time = update_book_event.book_event_time(year, month, day)
                        formatted_date = month + " " + day + " " + str(year)
                        formatted_time = str(time[0]) + " " + str(time[1])
                        formatted_event_sche = formatted_date + " " + formatted_time
                        event_store[int(update_event) - 1][2] = formatted_event_sche
                        update_loop = False
                        break

                    else:
                        print("Invalid Choose. try Again.")
            else:
                print("Please input the correct corresponding number.")

# -==============================-EDIT EVENT STATUS-==============================-

    elif user_choose == "4":
        change_event_status(event_store, ['Active', 'Cancelled'])  # Call your function here

# -==============================-DELETE AN EVENT-==============================-

    elif user_choose == "5":
        display_events(event_store)
        delete_confirmation = input("Enter the number of the event you want to delete: ").strip()

        if delete_confirmation.isdigit() and 1 <= int(delete_confirmation) <= len(event_store):
            confirm_delete = input("Are you sure? Details will be deleted permanently. To proceed, type 'yes': ").strip().lower()
            if confirm_delete == "yes":
                del event_store[int(delete_confirmation) - 1]
                print("Event deleted successfully.")
            else:
                print("Deletion cancelled.")
        elif delete_confirmation.lower() == "cancel":
            print("Deletion cancelled.")
        else:
            print("Invalid input.")

# -==============================-EXIT-==============================-

    elif user_choose == "6":
        break

    else:
        print("Invalid Choose. Try Again!")

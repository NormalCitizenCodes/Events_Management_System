import datetime


def display_menu():  # This function display the menu that user can choose
    print("+----------------------+-----+")
    print("| Display Event        |  1  |")
    print("| Book Event           |  2  |")
    print("| Update Event         |  3  |")
    print("| Change Event Status  |  4  |")
    print("| Delete Event         |  5  |")
    print("| Exit                 |  6  |")
    print("+----------------------+-----+")


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
        event_name = input("Event name: ")
        event_venue = input("Event venue: ")
        return [event_name, event_venue]

    def book_event_year(self):
        while True:
            event_year = input("Enter event year: ").strip()
            if event_year.isdigit() and int(event_year) >= self.current_year:
                return int(event_year)
            else:
                print("Invalid Year. Try Again.")

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
            event_month = input("Enter event month: ").strip().capitalize()
            if event_month in month_abr or event_month in month_not_abr:
                if user_event_year == self.current_year:
                    if event_month in month_abr and month_abr.index(event_month) >= month_abr.index(self.current_month):
                        return month_abr[month_abr.index(event_month)]
                    elif event_month in month_not_abr and month_not_abr.index(event_month) >= month_abr.index(
                            self.current_month):
                        return month_abr[month_not_abr.index(event_month)]
                    else:
                        print("Invalid Month. Try Again.")
                else:
                    if event_month in month_abr:
                        return month_abr[month_abr.index(event_month)]
                    elif event_month in month_not_abr:
                        return month_abr[month_not_abr.index(event_month)]
                    else:
                        print("Invalid Month. Try Again.")
            else:
                print("Invalid Month. Try Again.")

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
            event_days = input("Enter event day: ").strip()

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
                        print("Invalid Day. Try Again.")
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
                        print("Invalid Day. Try Again.")
            else:
                print("Dota 3")
                print("Invalid Day. Try Again.")

    def book_event_time(self, user_event_year, user_event_month, user_event_day):
        print("Ex valid format: 3 PM")
        while True:
            event_time = input("Enter event time ").strip()
            event_time_list = event_time.split()
            hour = event_time_list[0]
            if len(event_time_list) == 2:
                meantime = event_time_list[1].upper()
                if (hour.isdigit() and int(hour) < 13) and (meantime == "AM" or meantime == "PM"):
                    hour = int(hour)
                    if (user_event_year == self.current_year and user_event_month == self.current_month and
                            int(user_event_day) == self.current_day):
                        if meantime == "PM":
                            hour = hour + 12
                            if hour > self.current_hour:
                                return [hour - 12, meantime]
                            else:
                                print("Invalid PM time")
                        else:
                            if hour == 12:
                                hour = hour - 12
                            if hour > self.current_hour:
                                return [hour, meantime]
                            else:
                                print("Invalid AM time")
                    else:
                        return [hour, meantime]
                else:
                    print("Invalid time format")
            else:
                print("Invalid time format")


event_store = []
while True:
    display_menu()
    user_choose = input("Choose: ")

    if user_choose == "1":

        if len(event_store) == 0:
            print("You didn't save any event.")
        else:
            event_store.sort(key=lambda x: datetime.datetime.strptime(x[2], "%b %d %Y %I %p"))
            print("+----------------------------------------+---------------------+---------------------+")
            print("│               EVENT NAME               │      EVENT VENUE    │       SCHEDULE      │")
            print("+----------------------------------------+---------------------+---------------------+")
            for display_info in range(len(event_store)):
                name = event_store[display_info][0].center(40)
                venue = event_store[display_info][1].center(21)
                schedule = event_store[display_info][2].center(21)
                print(f"│{name}│{venue}│{schedule}│")
            print("+----------------------------------------+---------------------+---------------------+")

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
        event_info = [name_venue[0], name_venue[1], formatted_event_sche]
        event_store.append(event_info)

    elif user_choose == "3":
        pass
    elif user_choose == "4":
        pass
    elif user_choose == "5":
        pass
    elif user_choose == "6":
        pass
    else:
        print("Invalid Choose. Try Again!")

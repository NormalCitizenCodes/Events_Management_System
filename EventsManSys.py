import datetime


def current_date():  # This function return the current date ( Month Day Year)
    today_date = datetime.datetime.now()
    year = int(today_date.strftime("%Y"))
    month = today_date.strftime("%b")
    day = int(today_date.strftime("%d"))
    formatted_date = [month, day, year]
    return formatted_date


def display_menu():  # This function display the menu that user can choose
    print("+----------------------+-----+")
    print("| Display Event        |  1  |")
    print("| Book Event           |  2  |")
    print("| Update Event         |  3  |")
    print("| Change Event Status  |  4  |")
    print("| Delete Event         |  5  |")
    print("| Exit                 |  6  |")
    print("+----------------------+-----+")


def book_event_year():  # This function validate the year
    cmp_month, cmp_day, cmp_year = current_date()
    year_loop = True
    while year_loop:
        event_year = input("Enter event year: ").strip()
        if event_year.isdigit() and int(event_year) >= cmp_year:
            return int(event_year)
        else:
            print("Invalid Year. Try Again.")


def book_event_month(user_event_year):  # This function validate the month
    cmp_month, cmp_day, cmp_year = current_date()
    month_abr = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    month_not_abr = [
        "January", "February", "March", "April", "May",
        "June", "July", "August", "September", "October",
        "November", "December"
    ]

    month_loop = True
    while month_loop:
        event_month = input("Enter event month: ").strip().capitalize()
        if event_month in month_abr or event_month in month_not_abr:

            if user_event_year == cmp_year:
                if event_month in month_abr and month_abr.index(event_month) >= month_abr.index(cmp_month):
                    return event_month
                elif event_month in month_not_abr and month_not_abr.index(event_month) >= month_abr.index(cmp_month):
                    return event_month
                else:
                    print("Invalid Month. Try Again.")
            else:
                return event_month
        else:
            print("Invalid Month. Try Again.")


def book_event_day(user_event_year, user_event_month):  # This function validate the event day
    cmp_month, cmp_day, cmp_year = current_date()
    today_date = datetime.datetime.now()
    month_fullname = today_date.strftime("%B")

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

    day_loop = True
    while day_loop:
        event_days = input("Enter event day: ").strip()

        if event_days.isdigit():

            if user_event_year == cmp_year and user_event_month == cmp_month or user_event_month == month_fullname:
                if user_event_month in month_31_day and cmp_day <= int(event_days) <= 31:
                    return event_days
                elif user_event_month in month_30_day and cmp_day <= int(event_days) <= 30:
                    return event_days
                elif user_event_month in month_spec_day and int(user_event_year) % 4 == 0 and cmp_day <= int(event_days) <= 29:
                    return event_days
                elif user_event_month in month_spec_day and int(user_event_year) % 4 != 0 and cmp_day <= int(event_days) <= 28:
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
            print("Invalid Day. Try Again.")


def book_event():  # This function use for event necessary information
    event_name = input("Enter event name: ")
    event_venue = input("Enter event venue: ")
    event_year_fun = book_event_year()
    event_month_fun = book_event_month(event_year_fun)
    event_day_fun = book_event_day(event_year_fun, event_month_fun)
    formatted_year = event_month_fun + " " + event_day_fun + " " + str(event_year_fun)
    book_info = [event_name, event_venue, formatted_year]
    return book_info


event_store = []

print("Event Management System.\n")
cur_month, cur_day, cur_year = current_date()
print("Current Date:", cur_month, cur_day, cur_year, "\n")
display_menu()

loop_control = True
while loop_control:
    user_choose = input("Choose: ")

    if user_choose == "1":
        if len(event_store) == 0:
            print("Save event is empty")
        else:
            for display_info in range(len(event_store)):
                print("Event Name:", event_store[display_info][0])
                print("Event Venue:", event_store[display_info][1])
                print("Event Date:", event_store[display_info][2])

    elif user_choose == "2":
        event_store.append(book_event())
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

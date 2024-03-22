import datetime


def current_date():  # This function return the current date ( Month Day Year)
    today_date = datetime.datetime.now()
    year = today_date.strftime("%Y")
    month = today_date.strftime("%m")
    day = today_date.strftime("%d")
    formatted_date = month + " " + day + " " + year
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


print("Event Management System.\n")
print("Current Date:", current_date(), "\n")
display_menu()

loop_control = True
while loop_control:
    user_choose = input("Choose: ")

    if user_choose == "1":
        pass
    elif user_choose == "2":
        pass
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
        
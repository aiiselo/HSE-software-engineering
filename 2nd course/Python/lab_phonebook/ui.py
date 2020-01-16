import sqlite3
import phonebook

#Вывод меню
def print_menu():
    print('\033[1mWhat do you want to do now?\033[0m')
    print('[1] Print all notes in the phone book')
    print('[2] Add new record to the phone book')
    print('[3] Delete a record in the phone book')
    print('[4] Search info about a phone number')
    print('[5] Lookup age of person in the phone book')
    print('[6] Edit a record in the phone book')
    print('[7] <= Exit and save')
    print()


conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS phonebook (name text, surname text, phone text, bday date)""")
conn.commit()

choice = "0"
print('\033[1mHello!\033[0m')

while choice != "7":
    print_menu()
    choice = input("Type in a number (1-7): ")
    if choice == "1":
        phonebook.print_pb(cursor)
    elif choice == "2":
        phonebook.add_to_pb(cursor)
        conn.commit()
    elif choice == "3":
        phonebook.delete_from_pb(cursor)
        conn.commit()
    elif choice == "4":
        phonebook.search_in_pb(cursor)
    elif choice == "5":
        phonebook.check_age(cursor)
    elif choice == "6":
        phonebook.edit_pb(cursor)
        conn.commit()
    elif choice != "7":
        print("Command was not found, please enter command from prompt below")
conn.close()
print('\033[1mGoodbye!\033[0m')

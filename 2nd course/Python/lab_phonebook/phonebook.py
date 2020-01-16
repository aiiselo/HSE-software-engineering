import sqlite3
import datetime


#Вывод всех записей в телефонной книге по алфавиту (имена)
def print_pb(cursor):
    print('\033[1mYou have chosen "Print all notes in the phone book":\033[0m')
    print('\033[1m')
    a = ['Name', 'Surname', 'Number', 'Birthday']
    for i in a:
        print(i.rjust(20), end='')
    print('\033[0m')
    for row in cursor.execute("SELECT name, surname, phone, bday FROM phonebook ORDER BY name").fetchall():
        for i in row:
            print(i.rjust(20), end='')
        print()


#Добавление новой записи в базу данных
def add_to_pb(cursor):
    conn = sqlite3.connect('phonebook.db')
    print('\033[1mYou have chosen "Add new record to the phone book":\033[0m')
    while True:
        try:
            print('To do add new record enter the following information:')
            name = input('Enter name >> ')
            surname = input('Enter surname >> ')
            number = input('Enter telephone number >> ')
            birthdate = input('Enter date of birth (DD/MM/YYYY) >> ')

            isValidDate = True  # Проверка даты на корректность
            if birthdate != '':
                day, month, year = birthdate.split('/')
                try:
                    datetime.datetime(int(year), int(month), int(day))
                except ValueError:
                    isValidDate = False

            name = name.title()  #Автоматическое форматирование имени
            surname = surname.title()  #Автоматическое форматирование фамилии
            number = number.replace('+7', '8')  # +7 -> 8 #Автоматическое форматирование номера
            if number[0] == '7':  #Если начинается с 7
                arr = '8'
                arr += number[1:]
                number = arr
            if len(number) == 10 and number[0] == 9:  # если остальная часть (без +7/8)
                arr = '8'
                arr += number[0:]
                number = arr

            flag = False  #Проверка имени на уникальность
            for row in cursor.execute("SELECT name, surname FROM phonebook").fetchall():
                if row[0] == name and row[1] == surname:
                    flag = True
                    break

            if flag == True:  #Если нашли этого человека
                print('\033[1mThis person is already exists in your phone book.\033[0m\nYou can: \n')
                print('[1] Add another person')
                print('[2] Edit existing record')
                print('[3] <= Go back to menu and save changes')
                choice = input("Type in a number (1-3): ")
                if choice == '1':
                    add_to_pb(cursor)
                    break
                elif choice == '2':
                    edit_pb(cursor)
                    break
                elif choice == '3':
                    break

            if flag == False and len(number) == 11 and isValidDate == True:  #Если имя не нашли и дата с телефоном верная
                print('\033[1mA new entry has been added\033[0m\n')
                cursor.execute("""INSERT INTO phonebook VALUES (?, ?, ?, ?)""", (name, surname, number, birthdate))
                conn.commit()
                break
            else:
                if len(number) != 11:
                    print('The input of number is incorrect.\n')
                if isValidDate == False:
                    print('The input of birth date is incorrect. \n')
                print('Please, try again\n')
                continue
        except:
            print("\033[1mIncorrect input, please try again\033[0m")


#Удаление записи из базы данных
def delete_from_pb(cursor):
    conn = sqlite3.connect('phonebook.db')
    print('\033[1mYou have chosen "Delete a record in the phone book":\033[0m')
    while True:
        try:
            print('[1] Delete by name\n[2] Delete by phone number')
            choice = input()
            exit = False #Небольшой костыль для выхода из цикла
            if choice == '1':#Удаление по имени
                print('To do this please enter the following information:')
                name = input('Enter name >> ')
                surname = input('Enter surname >> ')
                flag = False  #Проверка имени, если есть - флаг true
                for row in cursor.execute("SELECT name, surname FROM phonebook").fetchall():
                    if row[0] == name and row[1] == surname:
                        flag = True
                        break
                while flag == False: #Если не нашли человека
                    print('\033[1mThere is no person of that name in your phone book.\033[0m\nYou can:')
                    print('[1] Delete another person')
                    print('[2] <= Go back to menu and save changes')
                    choice = input()
                    if choice == '1':
                        delete_from_pb(cursor)
                        break
                    elif choice == '2':
                        break
                if flag == True: #Если нашли - удаляем
                    cursor.execute("""DELETE FROM phonebook WHERE name = ? AND surname = ?""", (name, surname))
                    conn.commit()
                    print("\033[1mDeleted successfully\033[0m")
                break
            if choice == '2': #Удаление по номеру
                print('To do this please enter enter the following information:')
                number = input('Enter phone number >> ')
                flag = False  #Проверка номера на наличие
                for row in cursor.execute("SELECT * FROM phonebook WHERE phone = ?", (number,)).fetchall():
                    name = row[0]
                    surname = row[1]
                    if name != '' and surname != '':
                        flag = True #Если нашли номер
                        print('\033[1mDo you want to delete number of', name, surname, '? ([1] - Yes, [2] - No) >> \033[0m')
                        answer = input()
                        if answer == '1' or answer == 'Yes':#Принимаются оба варианта
                            cursor.execute("""DELETE FROM phonebook WHERE name = ? AND surname = ?""", (name, surname))
                            conn.commit()
                            res = input("\033[1mDeleted successfully. \033[1m\nDo you want to continue deleting numbers? ([1] - Yes, [2] - No) >> ")
                            if res == '2' or res == 'No':
                                exit = True
                                break
                            elif res == '1' or res == 'Yes':
                                exit = False
                                continue
                        elif answer == '2' or 'No':
                            continue
                if exit == True:
                    conn.commit()
                    break
                if flag == False: #Если не нашли челика
                    print('\033[1mThere is no person with that number in your phone book.\033[0m\n You can:')
                    print('[1] Delete another number')
                    print('[2] <= Go back to menu and save changes')
                    choice = input()
                    if choice == '1':
                        delete_from_pb(cursor)
                        break
                    elif choice == '2':
                        break
        except:
            print("\033[1mIncorrect input, please try again\033[0m")


#Поиск записей в базе по различным критериям
def search_in_pb(cursor):
    print('\033[1mYou have chosen "Search info about a phone number":\033[0m')
    while True:
        try:
            print('\033[1mHow do you want to search?:\033[0m')
            print()
            print('[1] Search by name')
            print('[2] Search by surname')
            print('[3] Search by number')
            print('[4] Search by date of birth')
            print('[5] Show records starting with letters ...')
            print('[6] <= Go back to menu and save changes')
            print()
            choice = input("Type in a number (1-6): ")

            if choice == '1': #Search by name
                print('\033[1mYou have chosen "Search by name":\033[0m')
                name = input('Enter name >> ')
                is_found = False
                print('\033[1mSearch results:\033[0m')
                for row in cursor.execute("""SELECT * FROM phonebook WHERE name=?""", (name,)).fetchall():
                    for i in row:
                        print(i.rjust(20), end='')
                        is_found = True
                    print()
                if is_found == False:
                    print('\033[1mThere are no records for this query\033[0m')

            elif choice == '2':#Search by surname
                print('\033[1mYou have chosen "Search by surname":\033[0m')
                surname = input('\nEnter surname >> ')
                is_found = False
                print('\033[1mSearch results:\033[0m')
                for row in cursor.execute("""SELECT * FROM phonebook WHERE surname=?""", (surname,)).fetchall():
                    for i in row:
                        print(i.rjust(20), end='')
                        is_found = True
                    print()
                if is_found == False:#Если ничего не нашли
                    print('\033[1mThere are no records for this query\033[0m')

            elif choice == '3': #Search by number
                print('\033[1mYou have chosen "Search by number":\033[0m')
                number = input('\nEnter number >> ')
                is_found = False
                print('\033[1mSearch results:\033[0m')
                for row in cursor.execute("""SELECT * FROM phonebook WHERE phone=?""", (number,)).fetchall():
                    for i in row:
                        print(i.rjust(20), end='')
                        is_found = True
                    print()
                if is_found == False:
                    print('\033[1mThere are no records for this query\033[0m')

            elif choice == '4':#Search by birthdate
                print('\033[1mYou have chosen "Search by birthdate":\033[0m')
                birthdate = input('\nEnter birth date >> ')
                is_found = False
                for row in cursor.execute("""SELECT * FROM phonebook WHERE bday=?""", (birthdate,)).fetchall():
                    for i in row:
                        print(i.rjust(20), end='')
                        is_found = True
                    print()
                if is_found == False:
                    print('\033[1mThere are no records for this query\033[0m')

            elif choice == '5': #Search by the first letters of name and surname
                print('\033[1mYou have chosen "Show records starting with letters":\033[0m')
                l_name = input('Enter first letters of the name>> ')
                l_surname = input('Enter first letters of the surname >> ')
                is_found = False
                if l_surname != '' and l_name != '':  # введены обе буквы
                    for row in cursor.execute(
                            "SELECT name, surname, phone, bday FROM phonebook ORDER BY name").fetchall():
                        if row[0][0] == l_name and row[1][0] == l_surname:
                            for i in row:
                                print(i.rjust(20), end='')
                                is_found = True
                            print()
                elif l_surname == '' and l_name != '':  # введена только первая буква
                    for row in cursor.execute(
                            "SELECT name, surname, phone, bday FROM phonebook ORDER BY name").fetchall():
                        if row[0][0] == l_name:
                            for i in row:
                                print(i.rjust(20), end='')
                                is_found = True
                            print()
                elif l_surname != '' and l_name == '':  # введена только вторая буква
                    for row in cursor.execute(
                            "SELECT name, surname, phone, bday FROM phonebook ORDER BY name").fetchall():
                        if row[1][0] == l_surname:
                            for i in row:
                                print(i.rjust(20), end='')
                                is_found = True
                            print()
                else:
                    print_pb(cursor)  # ничего не ввели
                    is_found = True
                if is_found == False:
                    print('\033[1mThere are no records for this query\033[0m')

            elif choice == '6':
                break
        except:
            print("\033[1mIncorrect input, please try again\033[0m")


#Редактирование записей в бд
def edit_pb(cursor):
    conn = sqlite3.connect('phonebook.db')
    print('\033[1mYou have chosen "Edit a record in the phone book":\033[0m')
    while True:
        try:
            print('To edit a record please enter the following information:')
            name = input('Enter name >> ')
            surname = input('Enter surname >> ')
            flag = False  # проверка имени
            for row in cursor.execute("SELECT name, surname FROM phonebook").fetchall():
                if row[0] == name and row[1] == surname:
                    flag = True
                    break
            if flag == False:
                print('\033[1mThere is no person of that name in your phone book.\033[0m You can:')
                print('[1] Change info about another person')
                print('[2] <= Go back to menu and save changes')
                choice = input()
                if choice == '1':
                    edit_pb(cursor)
                elif choice == '2':
                    break
            print('Please enter a field you want to edit.\n[1] Name\n[2] Surname\n[3] Number\n[4] Birth date\n[5] <= Go back to menu')
            choice = input("Type in a number (1-5): ")
            if choice == '1':
                new_name = input("Enter new name >> ")
                cursor.execute("""UPDATE phonebook SET name = ? WHERE name = ? AND surname = ?""",
                               (new_name, name, surname))
                conn.commit()
                print("\033[1mChanged successfully\033[0m")
            if choice == '2':
                new_surname = input("Enter new surname >> ")
                cursor.execute("""UPDATE phonebook SET surname = ? WHERE name = ? AND surname = ?""",
                               (new_surname, name, surname))
                conn.commit()
                print("\033[1mChanged successfully\033[0m")
            if choice == '3':
                new_number = input("Enter new number >> ")
                cursor.execute("""UPDATE phonebook SET phone = ? WHERE name = ? AND surname = ?""",
                               (new_number, name, surname))
                conn.commit()
                print("\033[1mChanged successfully\033[0m")
            if choice == '4':
                new_db = input("Enter new birth date >> ")
                cursor.execute("""UPDATE phonebook SET bday = ? WHERE name = ? AND surname = ?""",
                               (new_db, name, surname))
                conn.commit()
                print("\033[1mChanged successfully\033[0m")
            if choice == '5':
                break
            print('What do you want to do next?\n[1] Change something again\n[2] <= Go back to menu and save changes')
            choice = input("Type in a number (1 or 2): ")
            if choice == '1':
                continue
            if choice == '2':
                break
        except:
            print("\033[1mIncorrect input, please try again\033[0m")


#Вывод возраста человека
def check_age(cursor):
    print('\033[1mYou have chosen "Lookup age of person in the phone book":\033[0m')
    while True:
        try:
            print('Enter the name and surname of person who"s age you what to know:')
            name = input('Enter name >> ')
            surname = input('Enter surname >> ')
            temp = 0 #дата рождения
            is_found = False #если нашли в базе
            for row in cursor.execute("""SELECT * FROM phonebook WHERE name=? AND surname = ?""",
                                      (name, surname)).fetchall():
                temp = row[3]#получили дату
                is_found = True
                break
            if is_found == False or temp == '':
                print('\033[1mThere are no records for this query\033[0m')
            else:
                current_date = datetime.date.today()
                temp = temp.split('/')
                birthday = datetime.date(int(temp[2]), int(temp[1]), int(temp[0])) #переводим в нужный формат
                age = current_date - birthday
                age = str(age)
                res = int(int(age.split()[0]) / 365) #полное число лет
                print('\033[1m', end = '')
                print(name, surname, 'is', res, 'years old now')
                print('\033[0m', end='')
            print('\033[1mWhat do you want to do next?\033[0m\n[1] Learn age of another person\n[2] <= Go back to menu and save changes')
            choice = input("Type in a number (1 or 2): ")
            if choice == '1':
                continue
            if choice == '2':
                break
        except:
            print("\033[1mIncorrect input, please try again\033[0m")

import csv
import json
import os
import datetime


class DB(object):
    table = {}  # словарь: "book_id" - Запись в словарь
    field = {}  # словарь: "Поле" - "Список book_id с такими полями"
    name = ''  # название БД

    def __init__(self, name):  # создание базы данных
        self.name = name
        self.table = {}
        self.field = {}
        self.directory = ""

    def get_info_from_file(self, filename):
        if not os.path.exists(f'{filename}'):
            f = open(filename, 'w', encoding='utf-8')
            f.close()
        else:
            with open(filename) as json_file:
                file = json.load(json_file,
                                  object_hook=lambda d: {k if k.isdigit() else k: v for k, v in d.items()})
            self.table = file[0]
            self.field = file[1]

    def get_table_records(self):
        return list(self.table.values())

    def add_record(self, book_id, record):  # добавление записи в базу данных с проверкой уникальности
        if self.table.get(book_id) is None:
            self.table[book_id] = record
            for field in record.values():
                if field != book_id:
                    if self.field.get(field) is None:
                        self.field[field] = set()
                    self.field[field] = set(self.field[field])
                    self.field[field].add(book_id)
        else:
            raise Exception

    def re_record(self, book_id, record):  # переписать уже существующую запись (полностью)
        self.delete_by_book_id(book_id)
        self.add_record(book_id, record)

    def edit_record(self, book_id, key, new_value):  # редактирование записи по полю
        old_value = self.table[book_id][key]
        self.table[book_id][key] = new_value
        self.field[old_value].remove(book_id)
        if not self.field[old_value]:
            del self.field[old_value]
        if self.field.get(new_value) is None:
            self.field[new_value] = []
        self.field[new_value].append(book_id)

    def clear_db(self):  # очистить БД, но не удалить её
        self.table = {}
        self.field = {}

    def delete_db(self, filename):  # удалить БД полностью
        os.remove(filename)

    def delete_by_book_id(self, book_id):  # удаление записи из БД по book_id
        for value in set(self.table[book_id].values()):
            if value != book_id:
                self.field[value].remove(book_id)
                if not self.field[value]:
                    self.field.pop(value)
        self.table.pop(book_id)

    def delete_by_field(self, key):  # удаление записи из БД по значению некоторого поля (не book_id)
        book_ids = set(self.field[key]).copy()
        for book_id in book_ids:
            self.delete_by_book_id(book_id)

    def save_db(self, filename):  # сохранить БД в файл
        self.directory = filename
        info = list()
        info.append(self.table)
        self.field = {k:list(j) for k, j in self.field.items()}
        info.append(self.field)
        with open(filename, "w") as file:
            json.dump(list(info), file)

    def to_csv(self, filename, additional_naming=""):
        if additional_naming != "":
            filename = filename[:-5]+additional_naming+".csv"
        records = self.get_table_records()
        columns = ['id', 'title', 'author', 'year', 'price']
        with open( filename, 'w' ) as csvfile:
            writer = csv.DictWriter( csvfile, fieldnames=columns )
            writer.writeheader()
            for data in records:
                writer.writerow( data )

    def back_up(self, filename):
        self.to_csv(filename, "_backup")

    def deback_up(self, filename):
        self.clear_db()
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader( csvfile )
            for row in reader:
                self.add_record(row['id'], row)
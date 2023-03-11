import sqlite3
import os
import pandas as pd
from tabulate import tabulate as tb
from DataController import Data as dt

path = os.getcwd()    # .replace('\\', '\\\\')
filename = 'DataController\\Notepad.db'
filepath = os.path.join(path, filename)

def get_menu():
    list_menu = "Меню:\n" \
    "1 - Посмотреть все заметки\n" \
    "2 - Изменить заметку\n" \
    "3 - Добавить заметку\n" \
    "4 - Удалить заметку\n" \
    "5 - Экспортировать заметки в файл\n" \
    "\n" \
    "Введите номер действия, либо 'exit' или 'q' для завершения программы:\n"
    return list_menu

def get_caption(type, number=""):
    if type == 0:
        if number == 1:
            return "===> Укажите название заметки:\n"
        elif number == 2:
            return "===> Укажите тело заметки:\n"
    elif type == 1:
        if number == 0:
            return "===> Укажите id заметки:\n"
        elif number == 1:
            return "===> Укажите новое название заметки или не указывайте ничего, нажав ENTER:\n"
        elif number == 2:
            return "===> Укажите новое тело заметки или не указывайте ничего, нажав ENTER:\n"
    elif type == 2:
        return "\n===> Нет сохраненных заметок! <===\n"
    elif type == 3:
        return "\n===> Заметка успешно добавлена! <===\n"
    elif type == 4:
        return "\n===> Заметка успешно изменена! <===\n"
    elif type == 5:
        return "\n===> Заметка успешно  удалена! <===\n"
    elif type == 6:
        return "\n===> Операция не выполнена! <===\n"
    elif type == 7:
        return "===> Заметка с указанным id не найдена! <===\n"
    elif type == 8:
        return "===> Укажите тип формат для экспорта:\n0 - JSON\n1 - XML\n"
    elif type == 9:
        return "\n===> Заметки экспортированы! <===\n"

def get_view(type=999):
    data = dt.get_check_data()
    sort = ""
    if type == 0:

        if data > 1:
            sort = input("\nОтсортировать заметки по убыванию?\nВведите 1 - Да или 0 - Нет:\n")
            if sort != "1":
                sort = "ASC"
            else:
                sort = "DESC"

        # data = dt.get_data(1)
        # print("\n--------------------- СПИСОК ЗАМЕТОК -------------------------\n")
        # for r in data:
        #     print(f"ID:{r[0]}\nЗаголовок: {r[1]}\nТело заметки: {r[2]}\nВремя создания: {r[3]}\n")
        # print("--------------------------------------------------------------\n")

        print("\n--------------------- СПИСОК ЗАМЕТОК -------------------------\n")
        print(tb(dt.get_data_frame(sort), headers='keys', tablefmt='rounded_grid', stralign='center'))
        print("\n--------------------------------------------------------------\n")
        input("Нажмите любую клавишу чтобы продолжить...\n")

    if type == 999:
        pass


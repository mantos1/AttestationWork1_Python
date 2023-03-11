from DataController import Data as dt
from View import View as v


def run():
    dt.check_db()
    print("Заметки 1.0\n\n")

    answer = ''
    while answer != "exit" and answer != "q":
        answer = input(str(v.get_menu()))
        get_action(answer)


def get_action(type_action):
    id = ""
    if type_action == "1":
        data = dt.get_check_data()
        if data == 0:
            print(v.get_caption(2))
            return
        v.get_view(0)

    elif type_action == "2":
        data = dt.get_check_data()
        if data == 0:
            print(v.get_caption(2))
            return
        id = input(str(v.get_caption(1,0)))
        if id == "" or id.isdigit() != 1 or dt.get_check_data(id) == 0:
            print(v.get_caption(6))
            print(v.get_caption(7))
            return
        check = dt.update_note(id,input(str(v.get_caption(1,1))), input(str(v.get_caption(1,2))))
        if check == "true":
            print(v.get_caption(4))
        else:
            print(v.get_caption(6))

    elif type_action == "3":
        dt.insert_note(input(str(v.get_caption(0,1))), input(str(v.get_caption(0,2))))
        print(v.get_caption(3))

    elif type_action == "4":
        data = dt.get_check_data()
        if data == 0:
            print(v.get_caption(2))
            return
        check = dt.delete_note(input(str(v.get_caption(1,0))))
        if check == "true":
            print(v.get_caption(5))
        else:
            print(v.get_caption(6))
            print(v.get_caption(7))

    elif type_action == "5":
        data = dt.get_check_data()
        if data == 0:
            print(v.get_caption(2))
            return
        check = dt.export_into_file(input(str(v.get_caption(8))))
        if check == "true":
            print(v.get_caption(9))
        else:
            print(v.get_caption(6))
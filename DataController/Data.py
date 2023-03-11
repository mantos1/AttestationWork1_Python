import sqlite3
import json as jn
import xml.etree.ElementTree as ET
import csv
import os
import pandas as pd

path = os.getcwd()    # .replace('\\', '\\\\')
filename = 'DataController\\Notepad.db'
filepath = os.path.join(path, filename)
conn = sqlite3.connect(filepath)
cur = conn.cursor()

def create_tb():
    # cur.execute("drop table if exists Employee")
    # conn.commit()
    cur.execute("""CREATE TABLE IF NOT EXISTS notes(
       id INTEGER PRIMARY KEY,
       name TEXT,
       body TEXT,
       date_insert DATE );
    """)
    conn.commit()
    # conn.close()

def create_db():
    if not os.path.isfile(filepath):
        with open(filepath, "w") as write_file:
            write_file.writelines("")
    create_tb()

def check_db():
    create_db()

def get_check_data(id = ""):
    sql = "SELECT count(*) FROM notes"
    if id != "":
        sql = sql + f" WHERE id =  {id}"
    cur.execute(sql)
    data = cur.fetchall()
    for r in data:
        data_return = r[0]
    return data_return

def get_data_frame(sort="ASC", id ="", name=""):
    sql = "SELECT id as [ID]" \
        " ,name as [Название]" \
        " ,body as [Текст]" \
        " ,date_insert as [Время создания]" \
        "FROM notes WHERE 1=1 "
    if id != "":
        sql = sql + f"id = {id} "
    if name != "":
        sql = sql + f"lower(name) like lower('%{name}%'))"
    sql = sql + f"ORDER BY id {sort}"

    df = pd.read_sql_query(sql, conn)
    return df

def insert_note(name, body):
    cur.execute("SELECT * FROM notes")
    data = cur.fetchall()

    note_line = [(name, body)]
    cur.executemany("INSERT INTO notes (name, body, date_insert) VALUES(?, ?, datetime('now','localtime'))", note_line)
    conn.commit()

def update_note(id, name = "", body = ""):
    i = 0
    if name != "":
        name = f",name = '{name}'"
        i = 1
    if body != "":
        body = f",body = '{body}'"
        i = 1
    if i == 0 or id == "" or id.isdigit() != 1:
        return "false"
    cur.execute(f"UPDATE notes SET id = id {name} {body} where id = {id}")
    conn.commit()
    return "true"

def delete_note(id, name = "", body = ""):
    if id == "" or get_check_data(id) == 0:
        return "false"
    cur.execute(f"DELETE FROM notes where id = {id}")
    conn.commit()
    return "true"

def export_into_file(type = ""):
    # 0 - экспорт в new_data.json
    # 1 - экспорт в new_data.xml
    if type == "" or type.isdigit() != 1:
        return "false"

    cur.execute("SELECT * FROM notes ORDER BY name")
    data = cur.fetchall()
    if type == "0":
        with open("export_data.json", "w", encoding = "UTF8") as write_file:
            jsonfile = []
            for r in data:
                jsonfile.append({"ID": r[0], "name": r[1], "body": r[2], "date_create": r[3]})
            jn.dump(jsonfile, write_file, indent=4, ensure_ascii=False)
            return "true"
    if type == "1":
        root = ET.Element("root")
        for key, value in enumerate(data):
            item = ET.SubElement(root, "item", name = f"item{key+1}")
            ET.SubElement(item, "ID").text = str(value[0])
            ET.SubElement(item, "name").text =  str(value[1])
            ET.SubElement(item, "body").text =  str(value[2])
            ET.SubElement(item, "date_create").text = str(value[3])
        tree = ET.ElementTree(root)
        tree.write("export_data.xml", xml_declaration=True , encoding='utf-8')
        return "true"

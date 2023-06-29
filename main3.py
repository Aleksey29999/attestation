import csv
from csv import DictWriter
from os import path
import time
import datetime
file_base = "notes.csv"
file_base1 = "notes1.csv"
import shutil
last_id = 0
all_data = []
new_all_data={}

# открытие или создание файла
def open_file():
    if not path.exists(file_base):
       with open(file_base, "w", encoding="utf-8") as f:
            fieldnames = ['id', 'title','note', 'date']
            all_data= csv.DictWriter(f, delimiter= ",", lineterminator="\r", fieldnames=fieldnames )
            all_data.writeheader()
            pass

# Запись списка в файл 
def record_base(file_base,new_all_data): 
    with open(file_base, 'a', encoding="utf-8") as f:
        fieldnames = ['id', 'title','note', 'date']
        all_data= csv.DictWriter(f, delimiter= ",", lineterminator="\r", fieldnames=fieldnames )
        all_data.writerow(new_all_data)
        f.close()
 
# запись файла в список
def read_records(file_base):
    global last_id, all_data
    with open(file_base, 'r', encoding="utf-8") as f:
        all_data = csv.DictReader(f, delimiter=",")
        return all_data
    return all_data

# просмотреть все
def show_all():
    with open(file_base, encoding="utf-8") as f:
        all_data = csv.DictReader(f, delimiter=",")
        count = 0
        for row in all_data:
            
            print ( )
            print (f'id: {row["id"]}')
            print (f'Заголовок: {row["title"]}')
            print (f'Заметки: {row["note"]}')
            print (f'Дата и время: {row["date"]}')
            print ("______________________________")
                
     

# Добавить новый контакт
def add_new_note():
    global last_id 
    last_id = len(open(file_base).readlines())
    
    title =  input(f"Введите заголовок: ")
    note = input(f"Введите тело заметки: ")
    time = datetime.datetime.today()
    date =  time.strftime("%d.%m.%Y %H:%M:%S")
    new_all_data = {'id':last_id, 'title':title, 'note':note, 'date':date}
    record_base(file_base,new_all_data)
    return new_all_data

# удаление заметок 
def Delete():
    show_all()
    with open(file_base) as csvfile, open(file_base1, 'w') as outputfile:
        fieldnames = ['id', 'title','note', 'date']
        input_id = input('введите номер id удаляемой заметки: ')
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames, lineterminator="\r")
        for row in reader:
            if input_id not in row['id']:
                writer.writerow({'id':row['id'], 'title':row['title'], 'note':row['note'], 'date':row['date']})
    shutil.move(file_base1,file_base)            
    return 0

# поиск записи
def Search():
    global file_base  
    with open(file_base) as csvfile, open(file_base1, 'w') as outputfile:
        fieldnames = ['id', 'title','note', 'date']
        input_date = input('введите дату для поиска в формате d.m.y(пример 28.06.2023): ')
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if input_date in row['date']:
                print (f'id: {row["id"]}')
                print (f'Заголовок: {row["title"]}')
                print (f'Заметки: {row["note"]}')
                print (f'Дата и время: {row["date"]}')
                print ("______________________________")   


# Внесение изменений- меню
def Change_menu():
    play = True
    while play:
        answer = input("Change:\n"
                       "1. изменение заголовка\n"
                       "2. изменения тела записи\n"
                       "3. выход\n")
        match answer:
            case "1":
                Change_title()
            case "2":
                Change_note()
            case "3":
                play = False
            case _:
                print("Try again!\n")
  

# Изменение заголовка
def Change_title():
    show_all()
    with open(file_base) as csvfile, open(file_base1, 'w') as outputfile:
        fieldnames = ['id', 'title','note', 'date']
        input_id = input('введите номер id изменяемой заметки: ',)
        input_title = input('введите новое значение заголовка: ',)
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames, lineterminator="\r")
        for row in reader:
            if input_id not in row['id']:
                writer.writerow({'id':row['id'], 'title':row['title'], 'note':row['note'], 'date':row['date']})
            else : 
                row['title']= input_title
                time = datetime.datetime.today()
                row['date'] = time.strftime("%d.%m.%Y %H:%M:%S")
                writer.writerow({'id':row['id'], 'title':row['title'], 'note':row['note'], 'date':row['date']})    
    shutil.move(file_base1,file_base)      
             
     

# Изменение заметок
def Change_note():
    show_all()
    with open(file_base) as csvfile, open(file_base1, 'w') as outputfile:
        fieldnames = ['id', 'title','note', 'date']
        input_id = input('введите номер id изменяемой заметки: ',)
        input_note = input('введите новое значение заметки: ',)
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames, lineterminator="\r")
        for row in reader:
            if input_id not in row['id']:
                writer.writerow({'id':row['id'], 'title':row['title'], 'note':row['note'], 'date':row['date']})
            else : 
                row['note']= input_note
                time = datetime.datetime.today()
                row['date'] = time.strftime("%d.%m.%Y %H:%M:%S")
                writer.writerow({'id':row['id'], 'title':row['title'], 'note':row['note'], 'date':row['date']})    
    shutil.move(file_base1,file_base)   

# менюшка
def main_menu():
    play = True
    while play:
        open_file()
        read_records(file_base)
        answer = input("Записная книжка:\n"
                       "1. просмотреть все записи\n"
                       "2. добавить новую запись\n"
                       "3. поиск записи по дате \n"
                       "4. изменить запись\n"
                       "5. удалить запись\n"
                       "6. выход\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_note()
            case "3":
                Search()      
            case "4":
                Change_menu()
            case "5":
                Delete()
            case "6":
                play = False
            case _:
                print("Try again!\n")

main_menu()

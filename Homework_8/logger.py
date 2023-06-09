import os
from data_create import name_data, surname_data, phone_data, adress_data
file_name = 'data.txt'

def print_data():
    if os.path.exists(file_name):
       print('Вывод данных из файла:')
       with open(file_name, 'r', encoding='utf-8') as file:
           list_data = file.readlines()
           for element in list_data:
               print(element)
    else:
        print('Файл не существует!!!')


def input_data():
    print('Введите данные для записи в файл: ')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{name};{surname};{phone};{adress} \n')


def filter_data(filter_string):
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines()
            if ';' in filter_string:
                list_filter = filter_string.split(';')
            else:
                list_filter = [filter_string]
            is_found = False
            for element in list_data: 
                temp_record = element.split(';')
                count = 0
                for record in temp_record:
                    for element_filter in list_filter:
                        if element_filter.lower() in record.lower() and len(element_filter.lower()) == len(record.lower()):
                            count += 1
                if count == len(list_filter):
                    print(element)
                    is_found = True
        if not is_found:
            print('Такой записи нет!')


def change_data(old_element,new_element):
    with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines()
            if ';' in old_element:
                list_filter = old_element.split(';')
            else:
                list_filter = [old_element]
            is_found = False
            for element in list_data:
                temp_record = element.split(';')
                count = 0
                for record in temp_record:
                    for old_element in list_filter:
                        if old_element.lower() in record.lower()and len(old_element.lower()) == len(record.lower()):
                           old_element = new_element
                           count += 1
                if count == len(list_filter):
                    print(new_element)
                    is_found = True
    if not is_found:
            print('Такой записи нет!')
    


def remove_data(filter_string):
    with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines()
            if ';' in filter_string:
                list_filter = filter_string.split(';')
            else:
                list_filter = [filter_string]
            is_found = False
            for element in list_data: 
                temp_record = element.split(';')
                count = 0
                for record in temp_record:
                    for element_filter in list_filter:
                        if element_filter.lower() in record.lower() and len(element_filter.lower()) == len(record.lower()):
                            element_filter.remove(list_filter)
                            count += 1
                if count == len(list_filter):
                    print(element_filter)
                    is_found = True
    if not is_found:
            print('Такой записи нет!')


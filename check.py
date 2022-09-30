import json
def check_main_menu():
    while True:
        try:
            num = int(input('Введите номер пункта, который хотите выполнить: '))
            if 0<=num<=6:break
            else:
                print('Такого пункта меню нет!')
                print("\033[31m {}\033[0m".format('Такого пункта меню нет! Попробуйте снова.'))
                continue
        except ValueError:
            print("\033[31m {}\033[0m" .format('Вы ввели некорректное число! Попробуйте снова.'))


    return num

def check_search_menu():
    while True:
        try:
            num = int(input('Введите номер пункта, по которому вы хотите найти контакт: '))
            if 0<=num<=1:break
            else:
                print('Такого пункта меню нет!')
                print("\033[31m {}\033[0m".format('Такого пункта меню нет! Попробуйте снова.'))
                continue
        except ValueError:
            print("\033[31m {}\033[0m" .format('Вы ввели некорректное число! Попробуйте снова.'))


    return num

def check_directory():
    '''
    Проверка, пустой ли справочник.
    :return:
    '''
    try:
        with open('data_base.json', 'r') as f:
            phone_dir = json.load(f)
            return True
    except:
        print('Ваш справочник пока еще пустой!')
        return False

def check_menu_act_contact():
    while True:
        try:
            num = int(input('Введите номер пункта, который хотите выполнить: '))
            if 0<=num<=4:break
            else:
                print('Такого пункта меню нет!')
                print("\033[31m {}\033[0m".format('Такого пункта меню нет! Попробуйте снова.'))
                continue
        except ValueError:
            print("\033[31m {}\033[0m" .format('Вы ввели некорректное число! Попробуйте снова.'))


    return num

def check_menu_ch_con():
    while True:
        try:
            num = int(input('Введите номер пункта, который хотите выполнить: '))
            if 1<=num<=4:break
            else:
                print('Такого пункта меню нет!')
                print("\033[31m {}\033[0m".format('Такого пункта меню нет! Попробуйте снова.'))
                continue
        except ValueError:
            print("\033[31m {}\033[0m" .format('Вы ввели некорректное число! Попробуйте снова.'))


    return num
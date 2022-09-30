import json
def get_value():
    print('Для занесения контакта в справочник заполните поочередно данные: ')
    dict_ph = {}
    dict_ph['surname'] = input('Введите фамилию: ')
    dict_ph['name'] = input('Введите имя: ')
    dict_ph['tel'] = input('Введите номер: ')
    dict_ph['comment'] = input('Комментарий: ')
    print('#' * 50)
    return dict_ph

def show_contact(list_res):
    '''
    Выводит в консоль найденные контакты
    :param list_res:
    :return:
    '''
    print('Найдены следующие контакты: ')
    for num, i in enumerate(list_res):
        print(f'\033[30m\033[42m\033[4m Контакт № {num+1}\033[0m\n'
              f'Фамилия: {i["surname"]}\n'
              f'Имя: {i["name"]}\n'
              f'Телефон: {i["tel"]}\n'
              f'Статус: {i["comment"]}\n')

def show_all_contact():
    '''
    Выводит в консоль все контакты контакты
    :param list_res:
    :return:
    '''

    with open('data_base.json', 'r') as f:
            phone_dir = json.load(f)
    print('Найдены следующие контакты: ')
    for num, i in enumerate(phone_dir):
        print(f'\033[30m\033[42m\033[4m Контакт № {num+1}\033[0m\n'
              f'Фамилия: {i["surname"]}\n'
              f'Имя: {i["name"]}\n'
              f'Телефон: {i["tel"]}\n'
              f'Статус: {i["comment"]}\n')
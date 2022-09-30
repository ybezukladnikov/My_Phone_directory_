import json

def create(dict_ph):
    try:
        with open('data_base.json', 'r') as f:
            phone_dir = json.load(f)
    except:
        phone_dir = []

    phone_dir.append(dict_ph)
    with open('data_base.json', 'w') as file:
        json.dump(phone_dir, file, indent=2)
    print('\033[30m\033[42m\033[4m {}\033[0m'.format('Ваш контакт успешно '
                                                     'внесен в базу. Переводим '
                                                     'вас в начало меню'))
    print('#'*50)






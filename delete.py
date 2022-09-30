import json



def delete_contact(data):
    with open('data_base.json', 'r') as f:
            phone_dir = json.load(f)

    for i in range(len(phone_dir)):
        if phone_dir[i] == data[0]:
            phone_dir.pop(i)

    with open('data_base.json', 'w') as file:
        json.dump(phone_dir, file, indent=2)
    print('\033[30m\033[42m\033[4m {}\033[0m'.format('Ваш контакт успешно удален. Переводим '
                                                     'вас в начало меню'))

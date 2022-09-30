from datetime import datetime as dt


def create_contact(data):
    time = dt.now().strftime('%Y:%B:%d - %H:%M')
    with open('log.csv','a') as file:
        file.write('\n{};Create new contact;{}'.format(time,data))

def delete_contact(data):
    time = dt.now().strftime('%Y:%B:%d - %H:%M')
    with open('log.csv','a') as file:
        file.write('\n{};Delete contact;{}'.format(time,data))

def export_csv():
    time = dt.now().strftime('%Y:%B:%d - %H:%M')
    with open('log.csv','a') as file:
        file.write('\n{};Export all contact in .csv'.format(time))


def import_csv():
    time = dt.now().strftime('%Y:%B:%d - %H:%M')
    with open('log.csv','a') as file:
        file.write('\n{};Import all contact from .csv'.format(time))

def change_con(new_data):
    time = dt.now().strftime('%Y:%B:%d - %H:%M')
    with open('log.csv','a') as file:
        file.write('\n{};Contact change;new contact{}'.format(time,new_data))
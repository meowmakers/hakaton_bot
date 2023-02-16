import requests
import json

from for_dict import MyDataBoy


class GetAllMixin:                                 
    def get_all_todos(self, url):
        response = requests.get(url + 'todo/all')
        if response.status_code == 200:
            return json.loads(response.text)
            # return response.text
        return 'Сервер упал'


class CreateMixin:
    def create_todo(self, url, title, status=False):                   
        created = MyDataBoy(title=title, is_done=status)
        response = requests.post(url + 'todo/create', data=json.dumps(created.res))
       
        if response.status_code == 200:
            return '1'
        elif response.status_code == 422:
            return '422'
        return 0


class GetOneMixin:                                 
    def retrive_todo(self, url, id_: int):
        response = requests.get(url + f'todo/{id_}')
        if response.status_code == 200:
            return json.loads(response.text)
        elif response.status_code == 404:
            return 'Нет такой записи!'
    


class UpdateMixin:                                 
    def update_todo(self, url, id_, name, status=False):
        updated = MyDataBoy(title=name, is_done=status)

        response = requests.put(url + f'todo/{id_}/update',
                                data=json.dumps(updated.res))
        if response.status_code == 200:
            return 'Успешно обновлено :)'
        elif response.status_code == 404:
            return 'ID ненайден!\n Нажмите на кнопку повторно.'
        else:
            return 'Данные введены неверно!\nНажмите на кнопку повторно'


class DeleteMixin:                             
    def delete_todo(self, url, id_):
        response = requests.delete(url + f'todo/{id_}/delete')
        if response.status_code == 200:
            return 'Успешно удалено'
        elif response.status_code == 404:
            return 'ID не найден!'
        return 'Вводите цифры!'
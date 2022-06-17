'''описание кода'''
import requests
import json
from mixins import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin
from settings import settings

class Car:


    def create(self):
        data = {
            'fields': 
            {
                'марка': input('Введите марку '),
                'модель':input('Введите модель '),
                'год выпуска': input('Введите год выпуска '),
                'объем двигателя':input('Введите объем двигателя '),
                'цвет': input('Введите цвет '),
                'тип кузова': input('Выберитие тип кузова '),
                'пробег': input('Введите пробег '),
                'цена':input('Введите цену ')}, 
                'typecast': True}
        data = json.dumps(data)
        req = requests.post(url=settings.get_url, headers=settings.HEADERS, data=data)
        return req.json()


    def listing(self):
        print('Listing records...')
        req = requests.get(settings.get_url + settings.LIST_RECORDS_URL, headers=settings.HEADERS)
        return req.json()


    def retrieve(self, id_):
        print('Retrieving record...')
        req = requests.get(f'{settings.get_url}/{id_}', headers=settings.HEADERS)
        return req.json()
        

    def update(self, id_):
        data = {
            'fields': 
            {
                'марка': input('Введите марку '),
                'модель':input('Введите модель '),
                'год выпуска': input('Введите год выпуска '),
                'объем двигателя':input('Введите объем двигателя '),
                'цвет': input('Введите цвет '),
                'тип кузова': input('Введите тип кузова: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап '),
                'пробег': input('Введите пробег '),
                'цена':input('Введите цену ')}, 
                'typecast': True}
        data = json.dumps(data)
        req = requests.patch(f'{settings.get_url}/{id_}', headers=settings.HEADERS, data=data)
        return req.text             

    def delete(self, id_):
        print('Deleting record...')
        req = requests.delete(
            settings.get_url + f'/{id_}', 
            headers=settings.HEADERS)
        return req.json()

car = Car()
# print(car.listing())
# print(car.retrieve_record('rec1DWhiA9GFoBQwA'))
# print(car.create_record())
# print(car.update_record('recwgtdRyWmy1pMo5'))
# print(car.delete_record('rec49zaXqWDEHWCiM'))

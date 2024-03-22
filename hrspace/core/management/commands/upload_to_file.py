import csv
import json
import os
from pathlib import Path
from typing import Any

import requests
from clint.textui import colored
from django.apps import apps
from django.core.management.base import BaseCommand, CommandParser

PROJECT_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = os.path.join(PROJECT_DIR, 'dev_data')
API = 'https://api.hh.ru/'


class Command(BaseCommand):
    help = 'Загружает данные в файлы CSV и JSON в директорию ../dev_data/'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('model', type=str)

    def handle(self, *args: Any, **options: Any) -> str:
        model = options.get('model')
        model = self.check_model(model)
        file_path, mimetype = self.save_file(model)
        self.get_to_api_hh(model, file_path, mimetype)

    def check_model(self, model):
        model_list = apps.get_models()
        for ex_model in model_list:
            if ex_model.__name__ == model.capitalize():
                self.stdout.write(
                    colored.green('+++ Проверка имени Модели успешно завершена...'))
                return ex_model
        self.stderr.write(f'--- Модель {model} не найдена')
        raise SystemExit

    def save_file(self, model):
        mimetype = input(
            'Выберите тип файла. '
            'CSV или JSON: ')
        if mimetype.lower() not in ('csv', 'json'):
            self.stderr.write('--- Сохранение невозможно. '
                              f'Тип файла:{mimetype}. Не поддерживается.')
            raise SystemExit
        model_to_filename = {
            'City': f'cities.{mimetype}',
            'LineOfBusiness': f'line_of_buisness.{mimetype}',
            'Skill': f'skills.{mimetype}'
        }

        filename = self.get_filename(model, model_to_filename)
        file_path = os.path.join(DATA_DIR, filename)
        if os.path.exists(file_path):
            answer = input(f'По указаному пути: {file_path} '
                           'Существует файл, хотите продолжить и удалить? '
                           'Введите Д или Н: ')
            if answer.lower() != 'д':
                self.stderr.write('--- Запись невозможна. Удалите файл')
                raise SystemExit
            os.remove(file_path)
            self.stdout.write(
                colored.green('+++ Файл успешно удален'))
        file = open(file_path, 'a+')
        file.close()
        self.stdout.write(
            colored.green('+++ Новый файл успешно создан'))
        return file_path, mimetype

    def get_filename(self, model, model_to_filename):
        filename = model_to_filename.get(model.__name__)
        return filename

    def get_to_api_hh(self, model, file_path, mimetype):
        if model.__name__ == 'City':
            data = self.get_areas()
            if mimetype == 'csv':
                with open(file_path, 'a+', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
        if model.__name__ == 'Skill':
            ...
        if model.__name__ == 'LineOfBusiness':
            ...

    def get_areas(self):
        response = requests.get(f'{API}/areas')
        data = response.content.decode()
        response.close()
        js_object = json.loads(data)
        areas = []
        for k in js_object:
            for i in range(len(k['areas'])):
                if len(k['areas'][i]['areas']) != 0:
                    for j in range(len(k['areas'][i]['areas'])):
                        if k['id'] == '113':
                            areas.append([k['areas'][i]['areas'][j]['id'],
                                          k['areas'][i]['areas'][j]['name']])
                else:
                    if k['id'] == '113':
                        areas.append([k['areas'][i]['id'],
                                      k['areas'][i]['name']])
        return areas

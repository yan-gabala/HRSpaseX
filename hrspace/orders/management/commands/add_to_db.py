import csv
import json
import mimetypes
import os
from pathlib import Path
from typing import Any

from clint.textui import colored
from django.apps import apps
from django.core.management.base import BaseCommand, CommandParser
from progress.bar import Bar


PROJECT_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = os.path.join(PROJECT_DIR, 'dev_data')


class Command(BaseCommand):
    help = 'Загружает данные из файлов CSV и JSON, которые храняться в ../dev_data/'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file',
                            type=str,
                            help='Указывает на имя файла с расширением. Например file.csv')
        parser.add_argument('model',
                            type=str,
                            help='Указывает на модель в которую необходимо добавить данные. Например: city')

    def handle(self, *args: Any, **options: Any) -> str:
        file = os.path.join(DATA_DIR, options.get('file'))
        model = options.get('model')
        mimetype = self.check_file(file)
        model = self.check_model(model)
        self.clean_to_datebase(model)

        for i in Bar('Загрузка').iter(self.load_to_datebase(file, mimetype)):
            obj = model(**i)
            obj.save()
        self.stdout.write(
            colored.cyan('Запись в базу данных успешно завершена...'))

    def check_model(self, model):
        model_list = apps.get_models()
        for ex_model in model_list:
            if ex_model.__name__ == model.capitalize():
                self.stdout.write(
                    colored.green('+++ Проверка имени Модели успешно завершена...'))
                return ex_model
        self.stderr.write(f'--- Модель {model} не найдена')
        raise SystemExit

    def check_file(self, file):
        if not os.path.isfile(file):
            self.stderr.write(f'--- Файл {file} не найден')
            raise SystemExit
        self.stdout.write(
            colored.green('+++ Проверка пути файла успешно завершена...'))
        mimetype = mimetypes.MimeTypes().guess_type(file)[0]

        if mimetype not in ('text/csv', 'application/json'):
            self.stderr.write(
                f'--- Формат файла {file} не относится к CSV или JSON')
            raise SystemExit
        self.stdout.write(
            colored.green('+++ Проверка формата файла успешно завершена...'))

        return mimetype

    def clean_to_datebase(self, model):
        if model.objects.exists():
            answer = input(
                f'Таблица {model} содержит данные.'
                'Вы хотите очистить данные? Д или Н: ')
            if answer.lower() == 'д':
                model.objects.all().delete()
            else:
                self.stderr.write('--- Запись невозможна. Очистите таблицу')
                raise SystemExit

    def load_to_datebase(self, file, mimetype):
        with open(file, newline='', encoding='utf-8') as f:
            try:
                if mimetype == 'text/csv':
                    next(f, None)
                    data = csv.DictReader(
                        f, fieldnames=('id', 'name'))
                    print(data)
                else:
                    data = json.load(f)
            except (csv.Error, TypeError):
                self.stderr.write('--- Ошибка файла')
                raise SystemExit

            for i in data:
                yield i

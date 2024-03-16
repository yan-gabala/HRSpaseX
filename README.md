# Backend
![Лицензия](https://img.shields.io/github/license/HRSpaceX/backend)
![Code Quality](https://github.com/HRSpaceX/backend/actions/workflows/code_quality.yml/badge.svg?branch=dev)
![DRF](https://pypi-camo.freetls.fastly.net/18c2771271928b1071e8d436680f9a0abf272294/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f646a616e676f726573746672616d65776f726b2e737667)

## Документация для работы в команде

[![Code Style](https://img.shields.io/badge/Прочитать-Документацию_Code_Style-blue?style=for-the-badge)](https://github.com/HRSpaceX/backend/blob/e/chore/docs/.github/dev_docs/code_style_rules.md) [![Pull Request](https://img.shields.io/badge/Прочитать-Документацию_Pull_Request-2ea44f?style=for-the-badge)](https://github.com/HRSpaceX/backend/blob/e/chore/docs/.github/dev_docs/pull_requests_rules.md)

### Цель сервиса
Дать заказчикам возможность размещать заявку на подбор по трем моделям оплаты. Рекрутерам – откликаться и вести переписку с клиентами в рамках внутреннего чата, направлять резюме и регистрировать вышедшего сотрудника (дата выхода и прохождение испытательного срока). 

> На стадии разработки.
## Технологии
- Python
- Django Rest Framework

### Общая структура проекта:

```
├──.github/              # Файлы и настройки, связанные с GitHub/Github actions
├── hrspace/             # Backend приложения Django/DRF
│   ├── aссounts/        # Приложение аккаунтов [в разработке]
│   ├── api/             # API - программный интерфейс приложения [в разработке]
│   ├── bid/             # Приложение билдера заявки [в разработке]
│   ├── hrspace/         # Главная директория проекта [в разработке]
│   └── manage.py        # Исполняемый файл
├── .gitignore           # Файл со списком неотслеживаемых файлов и каталогов
├── LICENSE              # Лицензия проекта
├── requirements.txt     # Файл со списком зависимостей
├── setup.cfg            # Конфигурационный файл
└── example.env          # Файл примера для секретных переменных [в разработке]
```
## Установка для разработки:
- Клонируйте проект на свой компьютер:
```
git clone git@github.com:HRSpaceX/backend.git
```
- Установите и активируйте виртуальное окружение c Python 3.9
```
cd ./backend/ &&
py -3.9 -m venv venv
```
Для Windows:
```
source venv/Scripts/Activate
```
Для Linux
```
source venv/bin/activate
```
- Установите зависимости из файла requirements.txt
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
- Создайте переменные окружения в основной папке проекта "backend"
```
touch .env
```
- Добавьте ваши данные в файл .env
```
SECRET_KEY="Секретный код Django"
DEBUG=True
```
## Проект разрабатывали:

| <!-- -->      | <!-- -->        | <!-- -->      |
|:-------------:|:---------------:|:-------------:|

## Лицензия

Пожалуйста, ознакомьтесь с [MIT license](https://github.com/HRSpaceX/backend?tab=MIT-1-ov-file)

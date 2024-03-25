# Backend
![Лицензия](https://img.shields.io/github/license/HRSpaceX/backend)
![Code Quality](https://github.com/HRSpaceX/backend/actions/workflows/code_quality.yml/badge.svg?branch=dev)
![DRF](https://pypi-camo.freetls.fastly.net/18c2771271928b1071e8d436680f9a0abf272294/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f646a616e676f726573746672616d65776f726b2e737667)
![](https://camo.githubusercontent.com/8531ea80bc5e0ac96a01c1f2e18f168ca543ffd837522065bcf93f238774d4b8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c6174)


## Документация для работы в команде над проектом

[![Code Style](https://img.shields.io/badge/Прочитать-Документацию_Code_Style-blue?style=for-the-badge)](https://github.com/HRSpaceX/backend/blob/e/chore/docs/.github/dev_docs/code_style_rules.md) [![Pull Request](https://img.shields.io/badge/Прочитать-Документацию_Pull_Request-2ea44f?style=for-the-badge)](https://github.com/HRSpaceX/backend/blob/e/chore/docs/.github/dev_docs/pull_requests_rules.md)

## Ссылка на проект
[![Site](https://img.shields.io/badge/Перейти_на-Сайт-Cyanf?style=for-the-badge)](http://devinse.store/api/v1/)

### Цель сервиса
Дать заказчикам возможность размещать заявку на подбор по трем моделям оплаты. Рекрутерам – откликаться и вести переписку с клиентами в рамках внутреннего чата, направлять резюме и регистрировать вышедшего сотрудника (дата выхода и прохождение испытательного срока). 

> На стадии MVP.
## Технологии
- Python
- Django Rest Framework
- DRF Spectacular

### Общая структура проекта:

```
├──.github/              # Файлы и настройки, связанные с GitHub/Github actions
├── hrspace/             # Backend приложения Django/DRF
│   ├── aссounts/        # Приложение для переключения аккаунтов [в разработке]
│   ├── api/             # API - программный интерфейс приложения [в разработке]
│   ├── core/            # Приложение общего назначения для вспомогательных функций и процессоров
│   ├── hrspace/         # Главная директория проекта [в разработке]
│   ├── dev_data/        # Хранилище файлов для загрузки в базу данных
│   ├── orders/          # Приложение билдера заявки [в разработке]
│   ├── tests/           # Тесты приложения билдера заявки [в разработке]
│   ├──.dockerignore     # Конфигурационный файл, исключения Docker
│   ├──Dockerfile        # Конфигурационный файл Docker
│   └── manage.py        # Исполняемый файл
├── infra/               # Конфиг. файлы для инфраструктуры, переменные окружения
├── .gitignore           # Файл со списком неотслеживаемых файлов и каталогов
├── LICENSE              # Лицензия проекта
├── requirements.txt     # Файл со списком зависимостей
├── setup.cfg            # Конфигурационный файл
└── example.env          # Файл примера для секретных переменных [в разработке]
```
## Установка для разработки локальный запуск:
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

Для Windows:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
для Linux:
```
pip install --upgrade pip
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
[Подробнее в файле .env.example]
```
## Установка для разработки Docker:


## Установка приложения на выделенный сервер
Приложение может само разворачиваться и обновляться на выделенном сервере из этого репозитория.

1. Для этого нужно предварительно настроить сам сервер, а также секреты в репозитории (может только владелец).

2. Нужен сервер, видимый из интернета. У сервера должен быть известен публичный IP-адрес или имя хоста (напр. example.com)

3. На сервере должен быть установлен какой-нибудь из дистрибутивов Linux в качестве ОС

4. На сервере должен быть установлен Docker актуальной версии.

Docker нужно настроить так, чтобы он не требовал права (и пароль) супер-юзера. 


## Проект разрабатывали:

| <!-- --> | <!-- -->      | <!-- -->    |
|----------|---------------|-------------|
| Сергей Виноградов | Python-разработчик | [Cтраница GitHub](https://github.com/yan-gabala) |
| Юлия Семёнова | Python-разработчик | [Cтраница GitHub](https://github.com/JuliSem) |
| Эдуард Гумен | Python-разработчик | [Cтраница GitHub](https://github.com/hydrospirt) |


## Лицензия

Пожалуйста, ознакомьтесь с [MIT license](https://github.com/HRSpaceX/backend?tab=MIT-1-ov-file)

# Backend
![Лицензия](https://img.shields.io/github/license/HRSpaceX/backend)
![Code Quality](https://github.com/HRSpaceX/backend/actions/workflows/code_quality.yml/badge.svg?branch=dev)
![DRF](https://pypi-camo.freetls.fastly.net/18c2771271928b1071e8d436680f9a0abf272294/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f646a616e676f726573746672616d65776f726b2e737667)
[![CONTRIBUTING](https://camo.githubusercontent.com/8531ea80bc5e0ac96a01c1f2e18f168ca543ffd837522065bcf93f238774d4b8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c6174)](https://github.com/HRSpaceX/backend/blob/dev/CONTRIBUTING.md)


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
│   ├── api/             # API - программный интерфейс приложения [MVP]
│   ├── core/            # Приложение общего назначения для вспомогательных функций и процессоров
│   ├── hrspace/         # Главная директория проекта [MVP]
│   ├── dev_data/        # Хранилище файлов для загрузки в базу данных
│   ├── orders/          # Приложение билдера заявки [MVP]
│   ├──.dockerignore     # Конфигурационный файл, исключения Docker
│   ├──Dockerfile        # Конфигурационный файл Docker
│   └── manage.py        # Исполняемый файл
├── infra/               # Конфиг. файлы для инфраструктуры, переменные окружения
├── .gitignore           # Файл со списком неотслеживаемых файлов и каталогов
├── LICENSE              # Лицензия проекта
├── requirements.txt     # Файл со списком зависимостей
├── setup.cfg            # Конфигурационный файл
└── example.env          # Файл примера для секретных переменных
```

## Вспомогательные команды для загрузки данных с api.hh

Для скачивания в csv/json файл данных:
- Работает для трех моделей City, LineOfBusiness, Skill

```python
python manage.py upload_to_db model # вместо model подставить одну из моделей
# Например: python manage.py upload_to_db City

```
Для загрузки данных в базу:
- Работает для трех моделей City, LineOfBusiness, Skill

```python
python manage.py add_to_db filename.ext model # вместо model подставить одну из моделей / вместо filename.ext подставить файл с расширением
# Например: python manage.py add_to_db cities.csv City
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
DEBUG=False
[Подробнее в файле .env.example]
```
```
docker-compose build
```

```
docker-compose up
```

## Установка приложения на выделенный сервер

Приложение может само разворачиваться и обновляться на выделенном сервере из этого репозитория.

1. Для этого нужно предварительно настроить сам сервер, а также секреты в репозитории (может только владелец).

2. Нужен сервер, видимый из интернета. У сервера должен быть известен публичный IP-адрес или имя хоста (напр. example.com)

3. На сервере должен быть установлен какой-нибудь из дистрибутивов Linux в качестве ОС

4. На сервере должен быть установлен Docker актуальной версии.

Docker нужно настроить так, чтобы он не требовал права (и пароль) супер-юзера. 

> Написать

## Примеры запросов:

> Подробнее можно ознакомится в документации Redoc http://devinse.store/api/v1/schema/redoc/

> Подробнее можно ознакомится в документации Swagger http://devinse.store/api/v1/schema/swagger/

> Полные снимки документации находятся https://github.com/HRSpaceX/backend/tree/dev/.github/dev_docs/assets

#### Получение списка городов:

```
http://127.0.0.1:8000/api/v1/cities/
```

```json
[
{
"id": 0,
"name": "string"
}
]
```
#### Получение списка заявок:

```
http://127.0.0.1:8000/api/v1/orders/
```

```json
[
  {
    "id": 0,
    "name": "string",
    "line_of_business": "string",
    "city": "string",
    "work_format": "remote",
    "salary_from": "string",
    "salary_to": "string",
    "start_work_day": "14:15:22Z",
    "end_work_day": "14:15:22Z",
    "schedule": "full_day",
    "type_employment": "full",
    "business_trip": "yes",
    "amount_of_subordinate": "string",
    "features_vacancy": "string",
    "work_experience": "doesnot_matter",
    "skill": [
      "string"
    ],
    "education": "higher",
    "portfolio": "is_required",
    "amount_of_employees": "string",
    "award_option": "string",
    "award": "string",
    "start_work": "2019-08-24",
    "format_interview": "string",
    "start_interview": "2019-08-24",
    "amount_of_hr": "string",
    "hr_responsibility1": true,
    "hr_responsibility2": true,
    "hr_responsibility3": true,
    "hr_responsibility4": true,
    "hr_responsibility5": true,
    "hr_requirements": "string",
    "hr_requirements1": true,
    "hr_requirements2": true
  }
]
```

#### Для добавления заявки:

```
http://127.0.0.1:8000/api/v1/orders/
```

```json
{
  "name": "string",
  "work_format": "remote",
  "start_work_day": "14:15:22Z",
  "end_work_day": "14:15:22Z",
  "schedule": "full_day",
  "type_employment": "full",
  "business_trip": "yes",
  "features_vacancy": "string",
  "work_experience": "doesnot_matter",
  "skill": [
    "string"
  ],
  "education": "higher",
  "portfolio": "is_required",
  "start_work": "2019-08-24",
  "start_interview": "2019-08-24",
  "hr_responsibility1": true,
  "hr_responsibility2": true,
  "hr_responsibility3": true,
  "hr_responsibility4": true,
  "hr_responsibility5": true,
  "hr_requirements": "string",
  "hr_requirements1": true,
  "hr_requirements2": true
}
```


## Проект разрабатывали:

| <!-- --> | <!-- -->      | <!-- -->    |
|----------|---------------|-------------|
| Сергей Виноградов | Python-разработчик | [Cтраница GitHub](https://github.com/yan-gabala) |
| Юлия Семёнова | Python-разработчик | [Cтраница GitHub](https://github.com/JuliSem) |
| Эдуард Гумен | Python-разработчик | [Cтраница GitHub](https://github.com/hydrospirt) |


## Лицензия

Пожалуйста, ознакомьтесь с [MIT license](https://github.com/HRSpaceX/backend?tab=MIT-1-ov-file)

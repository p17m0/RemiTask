# RemiTask

Remi's test task.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

## Описание проекта

Тестовое задание Remi

## Установка проекта локально

* Склонировать репозиторий на локальную машину:

```bash
git clone https://github.com/skarabey147/foodgram-project-react.git
cd foodgram-project-react
```

* Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source env/bin/activate
```


* Перейти в директoрию и установить зависимости из файла requirements.txt:

```bash
cd backend/
pip install -r requirements.txt
```

* Выполните миграции:

```bash
python manage.py migrate
```

* Запустите сервер:

```bash
python manage.py runserver
```

## Запуск проекта в Docker контейнере

* Установите Docker.

Параметры запуска описаны в файлах `docker-compose.yml` и `nginx.conf` которые находятся в директории `infra/`.При необходимости добавьте/измените адреса проекта в файле `nginx.conf`

* Запустите docker compose:

```bash
docker-compose up -d --build
```

> После сборки появляются 1 контейнера:
>
> 1. контейнер приложения **backend**

* Примените миграции:

```bash
docker-compose exec backend python manage.py migrate
```

* Создайте администратора:

```bash
docker-compose exec backend python manage.py createsuperuser
```

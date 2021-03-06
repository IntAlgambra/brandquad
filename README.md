# Candyapi

Реализация тестового задания от Brandquad. django-приложение для мониторинга апач-логов.

## Требования

1. Docker

2. docker-compose

## Инструкции по деплою

1. Клонируем репозиторий

```
git clone https://github.com/IntAlgambra/brandquad.git
```

2. Переходим в папку проекта и создаем файл с переменными окружения .brandquad.env


3. Прописываем в .brandquad.env необходимые переменные окружения

```
DJANGO_SECRET_KEY=секретный ключ приложения Джанго
POSTGRES_USER=имя пользователя в БД Postgres
POSTGRES_PASSWORD=пароль пользователя в БД Postgres

```

4. Запускаем приложение  и производим миграции БД

```
sudo docker-compose up -d --build
sudo docker-compose run --rm backend python manage.py migrate
```

5. Добавляем суперпользователя


## Обновление приложения

1. Подтягиваем новую версию приложения из удаленного репозитория

```
git pull
```

2. Пересобираем контейнеры и запускаем миграции БД

```
sudo docker-compose up -d --build
sudo docker-compose run --rm backend python manage.py migrate
```

## Запуск парсера логов

```
sudo docker-compose run --rm backend python manage.py load_log <url to log file>
```


## Тесты

Для запуска тестов:

```
sudo docker-compose run --rm backend python manage.py test
```
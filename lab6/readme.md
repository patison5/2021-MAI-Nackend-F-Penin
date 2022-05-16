## Лабораторная работа №6

### Файл .env.dev
Содержит все необходимые переменные окружения для создания и работы контейнеров nginx, django и postgressql. Замечу, что superuser создается автоматически, данные супер-юзера также указываются в .env файле

Пример такого файла:
```
DEBUG=1
SECRET_KEY=django-insecure-n1ec(co@etx_89zsr$vrr-65ju*v!%kw52pe*qkecg1m$ixbe%2
DJANGO_ALLOWED_HOSTS=192.168.31.210
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=lab_6_db
SQL_USER=lab6_user
SQL_PASSWORD=lab6_password
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
DJANGO_SUPERUSER_USERNAME=kali
DJANGO_SUPERUSER_PASSWORD=kali
DJANGO_SUPERUSER_EMAIL=patison4@yandex.ru
```

#### Скачать и запустить контейнеры в фоновом режиме
```sh
docker-compose up -d --build 
```

#### Начать отслеживать состояние контейнера в интерактивном режиме (CMD+C - чтобы выйти)
```sh
docker-compose logs -f 
```


#### Дополнительно
Предполагается необходимость отключать flush и migrate при каждом запуске контейнера. Сделать это можно в файле django_project/entrypoing.sh

Команды для ручного запуска при необходимости
```sh
python manage.py flush --no-input
python manage.py migrate
```

#### Проверка базы данных
```sh
# Подключится к базе данных можно при помощи команды
docker-compose exec db psql --username=lab6_user --dbname=lab_6_db

# Отобразить базы данных
\l

# Выбрать базу данных
\c lab_6_db

# Показать таблицы
\dt 
```


#### Проверка, что том создан
```sh
docker volume inspect lab6_postgres_data 
```

Предполагаемый результат: 
```json
[
    {
        "CreatedAt": "2021-08-23T15:49:08Z",
        "Driver": "local",
        "Labels": {
            "com.docker.compose.project": "django-on-docker",
            "com.docker.compose.version": "1.29.2",
            "com.docker.compose.volume": "postgres_data"
        },
        "Mountpoint": "/var/lib/docker/volumes/django-on-docker_postgres_data/_data",
        "Name": "django-on-docker_postgres_data",
        "Options": null,
        "Scope": "local"
    }
]
```
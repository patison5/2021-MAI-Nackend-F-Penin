## Лабораторная работа №2

### Файл lab2_nginx_conf 
Содержит необходимые настройки конфигурации для nginx

### Файл setup.sh 
Отвечает за установку необходимого файла конфигурации nginx в системе

Важно! Данный скрипт удаляет все существующие активированные конфигурации по пути /etc/nginx/sites-enabled/
```
sudo rm /etc/nginx/sites-enabled/*
sudo cp ./lab2_nginx_conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/lab2_nginx_conf /etc/nginx/sites-enabled/
```

### Файл start_development.sh 
Запускает сборку в режиме разработки
```
python3 ./manage.py runserver 0.0.0.0:8000
```



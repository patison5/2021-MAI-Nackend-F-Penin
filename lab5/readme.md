## Лабораторная работа №5

### Файл lab2_nginx_conf 
Содержит необходимые настройки конфигурации для nginx

### Файл setup.sh 
Отвечает за установку необходимого файла конфигурации nginx в системе

Важно! Данный скрипт удаляет все существующие активированные конфигурации по пути /etc/nginx/sites-enabled/
```
sudo rm /etc/nginx/sites-enabled/*
sudo cp ./lab5_nginx_conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/lab5_nginx_conf /etc/nginx/sites-enabled/
```

### Файл start_development.sh 
Запускает сборку в режиме разработки
```
python3 ./manage.py runserver 0.0.0.0:8000
```


#### Программная инженерия (МАИ ПИ).postman_collection ####
Данный файл содержит в себе настройки для программы Postman, позволяющей быстро протестировать API приложения
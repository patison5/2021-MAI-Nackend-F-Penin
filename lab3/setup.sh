sudo rm /etc/nginx/sites-enabled/*
sudo cp ./lab3_nginx_conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/lab3_nginx_conf /etc/nginx/sites-enabled/

echo "Файл конфигурации был перезаписан по адресу: /etc/nginx/sites-enabled/"
ls -l /etc/nginx/sites-enabled/
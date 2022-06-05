sudo rm /etc/nginx/sites-enabled/*
sudo cp ./nginx.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/

echo "Файл конфигурации был перезаписан по адресу: /etc/nginx/sites-enabled/"
ls -l /etc/nginx/sites-enabled/

sudo /etc/init.d/nginx restartn
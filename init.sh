#!/bin/bash

sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn_wsgi.conf   /etc/gunicorn.d/wsgi.conf
sudo ln -s /home/box/web/etc/gunicorn_django.conf   /etc/gunicorn.d/django.conf
sudo /etc/init.d/gunicorn restart

#MySQL
mysql -uroot -e "CREATE DATABASE stepic_test;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'box';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_test.* TO 'box'@'localhost' WITH GRANT OPTION;"

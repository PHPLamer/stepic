#!/bin/bash

sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn_wsgi.conf   /etc/gunicorn.d/gunicorn_wsgi.conf
sudo /etc/init.d/gunicorn restart

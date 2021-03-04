"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_asgi_application()

# server {
# 	listen 443 default_server;
# 	listen [::]:443 default_server;
# 	ssl on;
# 	ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
# 	ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
#
# 	root /home/denis;
# 	index index.html index.htm index.nginx-debian.html;
# 	server_name _;
#
# 	location / {
#         	try_files $uri $uri/ /index.html;
#         }
#
# 	location /static {
#         	alias /home/backend/backend/img;
#     	}
#
# 	location /api {
#         	include proxy_params;
#         	proxy_pass http://unix:/run/gunicorn.sock;
#     	}
#
# 	location /admin {
#         	include proxy_params;
#         	proxy_pass http://unix:/run/gunicorn.sock;
#     	}
#
# 	location /img {
#         	alias /home/backend/backend/img;
#     	}
	# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
	#
	#location ~ \.php$ {
	#	include snippets/fastcgi-php.conf;
	#
	#	# With php7.0-cgi alone:
	#	fastcgi_pass 127.0.0.1:9000;
	#	# With php7.0-fpm:
	#	fastcgi_pass unix:/run/php/php7.0-fpm.sock;
	#}

	# deny access to .htaccess files, if Apache's document root
	# concurs with nginx's one
	#
	#location ~ /\.ht {
	#	deny all;
	#}
# }


# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#	listen 80;
#	listen [::]:80;
#
#	server_name example.com;
#
#	root /var/www/example.com;
#	index index.html;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}



export C_FORCE_ROOT="true"

a2enmod proxy proxy_http proxy_balancer lbmethod_byrequests

find /etc/apache2/sites-available/ -type f -exec a2ensite {} \;

mkdir -p /var/log/supervisord

python manage.py \
	collectstatic \
	--clear \
	--link \
	--noinput

python manage.py \
	migrate

supervisord -n -c /tmp/supervisord.conf

supervisorctl start all

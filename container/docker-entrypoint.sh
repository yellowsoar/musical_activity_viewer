export C_FORCE_ROOT="true"

a2enmod proxy proxy_http proxy_balancer lbmethod_byrequests

a2ensite mav.conf

apachectl start
mkdir -p /var/log/supervisord

python manage.py \
	collectstatic \
	--clear \
	--link \
	--noinput

python manage.py \
	migrate

uvicorn \
	musical_activity_viewer.asgi:application \
	--host 0.0.0.0 \
	--port 8000 \
	--access-log &
supervisord -n -c /tmp/supervisord.conf

python manage.py \
	qcluster
supervisorctl start all

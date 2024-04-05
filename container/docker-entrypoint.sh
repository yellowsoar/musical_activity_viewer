export C_FORCE_ROOT="true"

a2enmod proxy proxy_http proxy_balancer lbmethod_byrequests

a2ensite mav.conf

apachectl start

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

python manage.py \
	qcluster

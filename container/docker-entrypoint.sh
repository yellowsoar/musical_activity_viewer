export C_FORCE_ROOT="true"

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

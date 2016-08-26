web: gunicorn -b 0.0.0.0:10910 -w 4 codeformaine.wsgi
worker: celery -A codeformaine -l info worker

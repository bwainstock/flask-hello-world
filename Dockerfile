FROM python:3-onbuild
EXPOSE 8000
CMD gunicorn my_app:app --access-logfile '-' --bind 0.0.0.0:8000

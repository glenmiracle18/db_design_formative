pip insstall -r requirements.txt

python manage.py makemigrations

python manage.py migrate --fake

python manage.py collectstatic --noinput
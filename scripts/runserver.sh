#!/bin/sh

set -eux

#python manage.py wait_for_db
#python manage.py collectstatic --noinput
poetry run python manage.py migrate

script="
from accounts.models import CustomUser as User;

username = '$SPACERUNNER_ADMIN_USER';
password = '$SPACERUNNER_ADMIN_PASS';
email = '$SPACERUNNER_ADMIN_EMAIL';

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"
printf "$script" | poetry run python manage.py shell

poetry run uwsgi --ini uwsgi.ini

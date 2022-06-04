#!/bin/sh

set -eux

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

script="
import os
from accounts.models import CustomUser as User;

username = os.getenv(\"SPACERUNNER_ADMIN_USER\");
password = os.getenv(\"SPACERUNNER_ADMIN_PASS\");
email = os.getenv(\"SPACERUNNER_ADMIN_EMAIL\");

print(f\"Admin Username is: %s\", username)

if not User.objects.filter(username=username):
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"
printf "$script"
printf "$script" | python manage.py shell

uwsgi --ini uwsgi.ini

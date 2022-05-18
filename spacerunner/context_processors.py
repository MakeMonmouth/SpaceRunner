from django.conf import settings # import the settings file
from accounts.models import CustomUser as User

def setting_vars(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    settings_vars = {
            'SITE_NAME': settings.SITE_NAME,
            'TAG_LINE': settings.TAG_LINE,
            }
    return settings_vars

def registered_user_count(request):
   return { 'registered_users' : User.objects.all().count() }

def appname(request):
    app_name = request.path_info.split("/")[1]
    if app_name == "":
        app_name = settings.SITE_NAME
    else:
        app_name = app_name.capitalize()

    return {'appname': app_name}

from django.conf import settings # import the settings file
from django.apps import apps # Import the installed apps

def setting_vars(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    settings_vars = {
            'SITE_NAME': settings.SITE_NAME,
            'TAG_LINE': settings.TAG_LINE,
            'HEADER_BACKGROUND_IMAGE': settings.HEADER_BACKGROUND_IMAGE,
            'HEADER_BACKGROUND_ALT_TEXT': settings.HEADER_BACKGROUND_ALT_TEXT,
            }
    if hasattr(settings, "HEADER_CTA1_LINK"):
        settings_vars.update({"HEADER_CTA1_LINK": settings.HEADER_CTA1_LINK})
        settings_vars.update({"HEADER_CTA1_TEXT": settings.HEADER_CTA1_TEXT})
    if hasattr(settings, "HEADER_CTA2_LINK"):
        settings_vars.update({"HEADER_CTA2_LINK": settings.HEADER_CTA2_LINK})
        settings_vars.update({"HEADER_CTA2_TEXT": settings.HEADER_CTA2_TEXT})
    return settings_vars


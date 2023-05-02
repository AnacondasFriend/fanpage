from django.apps import AppConfig


class FanappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fanapp'

    def ready(self):
        import fanapp.signals

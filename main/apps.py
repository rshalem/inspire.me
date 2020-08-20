from django.apps import AppConfig


# application config file, this 'main' is used to define our installed apps like 'main,'
class MainConfig(AppConfig):
    name = 'main'

    # def ready(self):
    #     import main.signals
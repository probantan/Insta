from django.apps import AppConfig


class InstaConfig(AppConfig):
    name = 'Insta'
    def ready(self):
        import Insta.signals

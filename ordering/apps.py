from django.apps import AppConfig
#from suit.apps import DjangoSuitConfig
class OrderingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ordering'

def ready(self):
    import ordering.signals
'''
class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal
'''

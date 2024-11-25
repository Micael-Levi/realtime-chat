# project_name/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime_messaging.settings')

# Instância do Celery
app = Celery('realtime_messaging')

# Lê as configurações do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descobre e registra automaticamente as tarefas nos apps instalados
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

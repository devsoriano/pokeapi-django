from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configuración de Celery para usar las configuraciones de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

app = Celery('celery_app')

# Configura Celery para usar las opciones de settings.py con prefijo CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre tareas automáticamente dentro de las apps registradas
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

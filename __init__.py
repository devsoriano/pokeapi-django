from __future__ import absolute_import, unicode_literals

# Importa Celery para que esté disponible en todo el proyecto
from celery_app import app as celery_app

__all__ = ['celery_app']

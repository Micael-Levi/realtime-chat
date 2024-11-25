# project_name/__init__.py
from __future__ import absolute_import, unicode_literals

# Carrega o Celery app
from .celery import app as celery_app

__all__ = ['celery_app']

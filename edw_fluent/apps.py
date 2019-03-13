# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class EdwFluentConfig(AppConfig):
    name = 'edw_fluent'
    verbose_name = _("EDW fluent")

    def ready(self):
        # Импорт для инициализации сигнала. Не удалять!
        from .signals import handlers

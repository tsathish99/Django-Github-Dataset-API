# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class RestapiConfig(AppConfig):
    name = 'RestAPI'

    def ready(self):
        import RestAPI.signals

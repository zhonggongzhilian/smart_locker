# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from apps.home import views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('storage', views.storage, name='storage'),
                  path('storage_success', views.storage_success, name='storage_success'),
                  path('mine', views.mine, name='mine'),
                  path('mine_luggage', views.mine_luggage, name='mine_luggage'),
                  # Matches any html file
                  re_path(r'^.*\.*', views.pages, name='pages'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.home import views

urlpatterns = [
                  path('', views.home, name='home'),

                  path('storage', views.storage, name='storage'),
                  path('storage_success', views.storage_success, name='storage_success'),

                  path('mine', views.mine, name='mine'),
                  path('mine_luggage', views.mine_luggage, name='mine_luggage'),

                  path('manage_todo', views.manage_todo, name='manage_todo'),
                  path('select_locker', views.select_locker, name='select_locker'),
                  path('manage_saved', views.manage_saved, name='manage_saved'),
                  path('manage_done', views.manage_done, name='manage_done'),
                  path('manage_lockers', views.manage_lockers, name='manage_lockers'),
                  # Matches any html file
                  # re_path(r'^.*\.*', views.pages, name='pages'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

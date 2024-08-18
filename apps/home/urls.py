# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.home import views

urlpatterns = [

                  # The home page
                  path('', views.home, name='home'),

                  path('storage', views.storage, name='storage'),

                  path('mine', views.mine, name='mine'),

                  # Matches any html file
                  # re_path(r'^.*\.*', views.pages, name='pages'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

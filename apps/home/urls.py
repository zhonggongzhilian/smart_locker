# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.home, name='home'),

    path('storage', views.storage, name='storage'),

    path('mine', views.mine, name='mine'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]

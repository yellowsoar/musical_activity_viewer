"""
URL configuration for musical_activity_viewer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import opendata_tw.views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import (
    include,
    path,
    re_path,
)
from django.views.generic.base import RedirectView

urlpatterns = [
    re_path(
        r'^$',
        RedirectView.as_view(
            url='operation/',
            permanent=False,
        ),
    ),
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        'accounts/',
        include('allauth.urls'),
    ),
    path(
        'operation/',
        opendata_tw.views.activity_operation,
        name="operate_activity",
    ),
    path(
        'operation/update/<str:pk>',
        opendata_tw.views.update_activity,
        name="update_activity",
    ),
    path(
        'operation/delete/<str:pk>',
        opendata_tw.views.delete_activity,
        name="delete_activity",
    ),
    path(
        'api_list/',
        opendata_tw.views.DRFActivityList.as_view(),
        name="api_activity_filter_dev",
    ),
    re_path(
        r'^.*$',
        RedirectView.as_view(
            url='/',
            permanent=False,
        ),
    ),
]

urlpatterns += staticfiles_urlpatterns()

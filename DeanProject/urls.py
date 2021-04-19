"""DeanProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get, name='dashboard'),
    path('pending/', views.get, name='pending'),
    path('approved/', views.get, name='approved'),
    path('denied/', views.get, name='denied'),
    path('faculty/', views.get, name='faculty'),
    path('error/', views.error, name='error'),
    path('newform/', views.get, name='newform'),
    path('success/', views.get, name='success'),
    path('permitToRegister', views.get),
    path('addDropClass', views.get),
    path('UGGraduation', views.get),
    path('masterGraduation', views.get),
    path('degreeAudit', views.get),
    path('transcriptRequest', views.get),
    path('degreeAuditAmendmentRequest', views.get),
    path('', include("django.contrib.auth.urls")),
]

urlpatterns += staticfiles_urlpatterns()

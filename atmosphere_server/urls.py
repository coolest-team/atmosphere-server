"""atmosphere_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('getWind/', views.getWind),
    path('getCityPollutedHeat/', views.getCityPollutedHeat),
    path('getProvincePollutedHeat/', views.getProvincePollutedHeat),
    path('getCityPollutedParallel/', views.getCityPollutedParallel),
    path('getProvincePollutedParallel/', views.getProvincePollutedParallel),
    path('getProvinceGauge/', views.getProvinceGauge),
    path('getCityGauge/', views.getCityGauge),
    path('getTimeline/', views.getTimeline),
    path('getProvinceMap/',views.getProvinceMap),
    path('getCityMap/',views.getCityMap),
    path('getPrediction/',views.getPrediction),
    path('getProvinceTempa/', views.getProvinceTempa),
    path('getCityTempa/', views.getCityTempa),
]

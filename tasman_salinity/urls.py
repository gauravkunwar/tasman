"""tasman_salinity URL Configuration

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
from django.urls import path
from tasman import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('upload_data/', views.data_upload, name='data_upload'),
    path('admin/', admin.site.urls),
    path('table/', views.viewtable, name='table'),
    path('json/',views.viewjson, name='json'),
    path('chart/', views.viewchart, name='chart'),
    path('chart1/', views.viewchart1, name='chart1'),
    path('chart2/', views.viewchart2, name='chart2'),
    path('chart3/', views.viewchart3, name='chart3'),
    path('about/', views.about, name='about'),
    path('2g/', views.tech_2g, name='tech_2g'),
    path('3g/', views.tech_3g, name='tech_3g'),
    path('4g/', views.tech_4g, name='tech_4g'),
    path('NFC/', views.tech_NFC, name='tech_NFC'),
    path('ZigBee/', views.tech_ZigBee, name='tech_ZigBee'),
    path('WiFi/', views.tech_WiFi, name='tech_WiFi'),
    path('WiMax/', views.tech_WiMax, name='tech_WiMax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

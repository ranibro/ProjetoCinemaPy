from django.contrib import admin
from django.urls import path, include
from aplicativo.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include(urlpatterns))
]

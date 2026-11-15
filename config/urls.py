"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include
from home.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('menu/', include('menu.urls')),
    path('health/', health_check, name='health_check'),
]
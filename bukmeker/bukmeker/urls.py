from django.contrib import admin
from django.urls import path

from grant_app.views import gd

urlpatterns = [
    path('gd/', gd),
    path('admin/', admin.site.urls),
]

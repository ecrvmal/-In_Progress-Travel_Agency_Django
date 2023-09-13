from django.contrib import admin
from django.urls import path
from django.urls import include

import mainapp.views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.main, name='main'),    # name - название привязки для ссылок из др html страниц
    path('list_of_accommodations', include('mainapp.urls', namespace='acc')),    #  переход в маршруты приложения
]

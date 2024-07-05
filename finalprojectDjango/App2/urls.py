from django.contrib import admin
from django.urls import path, include
from def1.views import Home, About


urlpatterns = [
    path('admin/', admin.site.urls),
    # custom url
    path('', Home, name='Home'),
    path('about', About, name='About'),
]

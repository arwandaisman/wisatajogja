from django.contrib import admin
from django.urls import path, include
from home.views import home, utama


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('home/',home),
    path('utama/',utama),
    # path('', include('home.urls')),
    # path('datawisata/', include('datawisata.urls')),
    # path('admin/', include('admin.urls')),
]

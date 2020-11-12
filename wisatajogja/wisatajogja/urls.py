from django.contrib import admin
from django.urls import path, include
from home.views import home
from datawisata.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('home/',home),
    # path('utama/',utama),
    path('datawisata/tambah-wisata/', tambah_wisata),
    path('tambah-wisata/', tambah_wisata),
    path('datawisata/', datawisata),
    path('datawisata/<id>/edit',edit),
    path('datawisata/<id>/hapus',hapus),

    # path('<id>/hapus', hapus),
    # path('datawisata/ubah/<int:id>', edit, name='ubah'),
    # path('', include('home.urls')),
    # path('datawisata/', include('datawisata.urls')),
    # path('admin/', include('admin.urls')),
]

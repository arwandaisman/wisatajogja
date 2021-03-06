from django.contrib import admin
from datawisata.models import Datawisata,Jenis

class WisataAdmin(admin.ModelAdmin):
    list_display = ['nama_wisata','kabupaten','jml_pengunjung', 'lokasi', 'jenis_id']
    search_fields = ['nama_wisata','kabupaten']
    list_filter = ('kabupaten','jenis_id')
    list_per_page = 4

admin.site.register(Datawisata, WisataAdmin)
admin.site.register(Jenis)
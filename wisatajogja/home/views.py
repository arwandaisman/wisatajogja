from django.shortcuts import render
from home.models import Datawisata
form home.forms import FormDataWisata

def home(request):
    datawisatas = Datawisata.objects.all()
        
    konteks = {
        'datawisatas' : datawisatas, 
    }

    return render(request, 'halamanutama.html', konteks)

def utama(request):
    return HttpResponse('Halaman Utama')


def tambah_wisata(request):
    form = FormDataWisata
    konteks = {
        'form' : form,
    }
    return 
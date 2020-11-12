from django.shortcuts import render, redirect
from datawisata.models import Datawisata
from datawisata.forms import FormDataWisata




def datawisata(request):
    datawisatas = Datawisata.objects.all()
        
    konteks = {
        'datawisatas' : datawisatas, 
    }

    return render(request, 'datawisata.html', konteks)

def hapus(request, id):
    konteks = Datawisata.objects.filter(pk=id).delete()
    return redirect('datawisata/')


def tambah_wisata(request):
    if request.POST:
        form = FormDataWisata(request.POST)
        if form.is_valid():
            form.save()
            form = FormDataWisata()
            pesan = "Data Berhasil Disimpan"
            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambahWisata.html', konteks)
    else:
        form = FormDataWisata()
        pesan = "Silahkan isi data dengan benar"
        konteks = {
                'form' : form,
                'pesan' : pesan,
            }
    return render(request, 'tambahWisata.html', konteks)


def edit(request, id):
    
    template = 'edit.html'
    if request.POST:
        form = FormDataWisata(request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('ubah', id)
    else:
        form = FormDataWisata(instance=id)
        konteks = {
            'form':form,
            'datawisata':datawisata,
        }
    return render(request, template, konteks)
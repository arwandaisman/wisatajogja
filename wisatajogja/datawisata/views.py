from django.shortcuts import render, redirect
from datawisata.models import Datawisata
from datawisata.forms import FormDataWisata

def edit(request, id):
    datawisata = Datawisata.objects.get(pk=id)
    template = 'edit.html'
    if request.POST:
        form = FormDataWisata(request.POST, instance=datawisata)
        if form.is_valid():
            form.save()
            return redirect('ubah', pk=id)
    else:
        form = FormDataWisata(instance=datawisata)
        konteks = {
            'form':form,
            'datawisata':datawisata,
        }
    return render(request, template, konteks)


def datawisata(request):
    datawisatas = Datawisata.objects.all()
        
    konteks = {
        'datawisatas' : datawisatas, 
    }

    return render(request, 'datawisata.html', konteks)

def hapus(request,id):
    hapus = Datawisata.objects.filter(pk=id).delete()
    return render(request,'datawisata.html',hapus)


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
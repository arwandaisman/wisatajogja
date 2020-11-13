from django.shortcuts import render, redirect
from datawisata.models import Datawisata
from datawisata.forms import FormDataWisata




def datawisata(request):
    datawisatas = Datawisata.objects.all()
        
    konteks = {
        'datawisatas' : datawisatas, 
    }

    return render(request, 'datawisata.html', konteks)

# def hapus(request, id):
#     konteks = Datawisata.objects.filter(pk=id).delete()
#     return redirect('datawisata/')

def hapus(request, id_wisata):
    wisata = Datawisata.objects.filter(id=id_wisata)
    wisata.delete()
    return redirect('datawisata')
    

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


def edit(request, id_wisata):
    wisata = Datawisata.objects.get(id=id_wisata)
    template = 'edit.html'
    if request.POST:
        form = FormDataWisata(request.POST, instance=wisata)
        if form.is_valid():
            form.save()
            return redirect('ubah', id_wisata=id_wisata)
    else:
        form = FormDataWisata(instance=wisata)
        konteks = {
            'form':form,
            'datawisata':datawisata,
        }
    return render(request, template, konteks)
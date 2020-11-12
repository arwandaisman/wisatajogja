from django.shortcuts import render, redirect
from datawisata.models import Datawisata

def home(request):
    datawisatas = Datawisata.objects.all()
        
    konteks = {
        'datawisatas' : datawisatas, 
    }

    return render(request, 'halamanutama.html', konteks)


# def tambah_wisata(request):
#     form = FormDataWisata
#     konteks = {
#         'form' : form,
#     }
#     return render(request, 'tambahWisata.html', konteks)


# # def hapus(request,id):
# #     hapus = Datawisata.objects.filter(pk=id).delete()
# #     return render(request,'halamanutama.html',hapus)

# def edit(request,id):
#     edit = Datawisata.object.get(pk=id)
#     template = edit.html
#     if request.POST :
#         form = FormDataWisata(request.POST, instance=edit)
#         if form.is_valid():
#             form.save()
#             return redirect('edit', id=id)
#     else :
#         form = FormDataWisata(instance=edit)
#         konteks = {
#             'form' : form,
#             'edit' : edit,
#         }
#     return render(request, template, konteks)
from django.forms import ModelForm
from django import forms
from datawisata.models import Datawisata

class FormDataWisata(ModelForm):
    class Meta :
        model = Datawisata
        fields = '__all__'

        widgets = {
            'nama_wisata' : forms.TextInput({'class':'form-control'}),
            'kabupaten' : forms.TextInput({'class':'form-control'}),
            'jml_pengunjung' : forms.NumberInput({'class':'form-control'}),
            'lokasi' : forms.TextInput({'class':'form-control'}),
            'jenis_id' : forms.Select({'class':'form-control'}),
        }
from django.forms import ModelForm
from home.models import Datawisata

class FormDataWisata(ModelForm):
    class Meta :
        model = Datawisata
        fields = '__all__'
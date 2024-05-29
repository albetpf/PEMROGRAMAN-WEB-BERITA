from django import forms
from berita.models import Artikel
from django.contrib.auth.models import User

class ArtikelForm(forms.ModelForm):

    class Meta:
        model = Artikel
        fields = ('judul', 'isi', 'kategori', 'thumbnail')
        widgets = {

            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),
        
            "isi" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                }),

            "kategori" : forms.Select(
                attrs={
                    'class': 'form-control',
                }),
        }    
        
class EditProfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        

# myproject/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from berita.models import Artikel, Kategori

def home(request):
    template_name = "halaman/index.html"
    kategori = request.GET.get('kategori')
    if kategori is None:
        print("ALL")
        data_artikel = Artikel.objects.all()
        menu_aktif = "ALL"
    else:
        print("Bukan ALL")
        try:
            get_kategori = Kategori.objects.get(nama=kategori)
            data_artikel = Artikel.objects.filter(kategori=get_kategori)
            menu_aktif = kategori
        except ObjectDoesNotExist:
            menu_aktif = "ALL"
            data_artikel = []

    data_kategori = Kategori.objects.all()
    context = {
        'title': 'selamat datang',
        'data_artikel': data_artikel,
        'data_kategori': data_kategori,
        'menu_aktif': menu_aktif
    }
    return render(request, template_name, context)

def about(request):
    template_name = "halaman/about.html"
    context = {
        'title': 'selamat datang',
        'umur': 20,
    }
    return render(request, template_name, context)

def contact(request):
    template_name = "halaman/contact.html"
    context = {
        'title': 'selamat datang',
        'umur': 20,
    }
    return render(request, template_name, context)

def detail_artikel(request, slug):
    template_name = 'halaman/detail_artikel.html'
    artikel = get_object_or_404(Artikel, slug=slug)
    print(artikel.author)
    context = {
        'title': artikel.judul,
        'artikel': artikel
    }
    return render(request, template_name, context)

# Views for User Profile
def profil_pengguna(request, user_id):
    try:
        user = User.objects.get(pk=user_id)  # Use `get` for efficiency
    except User.DoesNotExist:
        return render(request, '/', status=404)  # Handle non-existent user

    return render(request, 'dashboard/users/profil_pengguna.html', {'user': user})

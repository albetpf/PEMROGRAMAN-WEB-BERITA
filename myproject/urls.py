from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from myproject.views import home, about, detail_artikel, contact
from myproject.authentikasi import akun_login, akun_logout, akun_registrasi
from berita.views import edit_profile, user_list, user_profile

from berita.api import *

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('dashboard/', include("berita.urls")),
    path('artikel/<slug:id>/', detail_artikel, name="detail_artikel"),

    path('authentikasi/login/', akun_login, name="akun_login"),
    path('authentikasi/registrasi/', akun_registrasi, name="akun_registrasi"),
    path('authentikasi/logout/', akun_logout, name="akun_logout"),

    path('dashboard/users/edit_profile/<int:user_id>/', edit_profile, name='edit_profile'),
    path('dashboard/users/user_list/', user_list, name='user_list'),
    path('dashboard/users/profile/<int:user_id>/', user_profile, name='user_profile'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/artikel/list', api_artikel_list),
    path('api/author/list', api_author_list),
    path('api/kategori/list', api_kategori_list),
    path('api/kategori/add', api_kategori_add),
    path('api/artikel/list', api_artikel_list),
    path('api/kategori/detail/<int:id_kategori>', api_kategori_detail),
    path('api/artikel/detail/<int:id_artikel>', api_artikel_detail),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

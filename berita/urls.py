from django.urls import path
from berita import views  # Mengimpor views dari modul berita

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('kategori/list/', views.kategori_list, name="kategori_list"),
    path('kategori/add/', views.kategori_add, name="kategori_add"),
    path('kategori/update/<int:id_kategori>/', views.kategori_update, name="kategori_update"),
    path('kategori/delete/<int:id_kategori>/', views.kategori_delete, name="kategori_delete"),

    path('artikel/list/', views.artikel_list, name="artikel_list"),
    path('artikel/add/', views.artikel_add, name="artikel_add"),
    path('artikel/detail/<int:id_artikel>/', views.artikel_detail, name="artikel_detail"),
    path('artikel/update/<int:id_artikel>/', views.artikel_update, name="artikel_update"),
    path('artikel/delete/<int:id_artikel>/', views.artikel_delete, name="artikel_delete"),

]
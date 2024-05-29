from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

def akun_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    template_name = "halaman/login.html"
    pesan = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            pesan = "gagal login"
    context = {
        'pesan' : pesan
    }
    return render(request, template_name, context)

def akun_registrasi(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    pesan = ''
    template_name = "halaman/registrasi.html"
    if request.method == "POST":
        username = request.POST.get("username")
        nama_depan = request.POST.get("nama_depan")
        nama_belakang = request.POST.get("nama_belakang")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        print(username, nama_belakang, nama_depan, email, password1, password2)

        if password1 == password2:
            check_user = User.objects.filter(username=username)
            if check_user.count() == 0:
                user_simpan = User.objects.create(
                    username = username,
                    first_name = nama_depan,
                    last_name = nama_belakang,
                    email = email,
                    # password = password1
                    is_active = True
                )
                user_simpan.set_password(password1)
                user_simpan.save()

                return redirect("/")
            else:
                pesan = "username sudah digunakan"
        else:
            pesan = "password tidak sama"

    context = {
        'pesan': pesan
    }
    return render(request, template_name, context)


def akun_logout(request):
    logout(request)
    return redirect('/')

from django.shortcuts import render

# Vista Home
def login(request):

    return render(request, "usuarios/login.html" )

def logout(request):

    return render(request, "usuarios/logout.html" )

def register(request):

    return render(request, "usuarios/register.html" )
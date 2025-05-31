from django.shortcuts import render

# Vista Home
def home(request):

    return render(request, "home/prueba_home.html" )

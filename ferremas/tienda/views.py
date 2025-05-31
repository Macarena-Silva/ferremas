from django.shortcuts import render

# Vista Tienda
def home(request):

    return render(request, "tienda/tienda.html")
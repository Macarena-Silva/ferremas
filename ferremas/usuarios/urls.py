from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin, name='admin'),
    path('bodeguero/', views.bodeguero, name='bodeguero'),
    path('contador/', views.contador, name='contador'),
]
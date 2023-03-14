from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.base, name="base"),
    path('dashboard', view=views.Dashboard, name="Dashboard"),
    path('rutien', view=views.Ruttien, name="Ruttien"),
    path('naptien', view=views.Naptien, name="Naptien"),
    path('thongtin', view=views.InforUser, name="Thongtin"),

]
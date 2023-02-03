from django.shortcuts import render,HttpResponse
from .models import InfoUser, HistoryTransaction
from django.contrib.auth.decorators import login_required
# Create your views here.
def base(request):
    return render(request, "manaTransaction/base.html")


def Dashboard(request):
    return render(request,"manaTransaction/dashboard.html")


def Ruttien(request):
    return render(request, "manaTransaction/ruttien.html")

def Naptien(request):
    return render(request, "manaTransaction/naptien.html")

def InforUser(request):
    return render(request, "manaTransaction/inforuser.html")
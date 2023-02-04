from django.shortcuts import render,HttpResponse
from .models import InfoUser, HistoryTransaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def base(request):
    return render(request, "manaTransaction/base.html")


def Dashboard(request):
    user_id = User.objects.get(username = "test@1").id
    his_users = HistoryTransaction.objects.filter(user = user_id)
    return render(request,"manaTransaction/dashboard.html",{"datas":his_users})


def Ruttien(request):
    return render(request, "manaTransaction/ruttien.html")

def Naptien(request):
    return render(request, "manaTransaction/naptien.html")

def InforUser(request):
    return render(request, "manaTransaction/inforuser.html")
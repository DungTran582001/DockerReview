from django.shortcuts import render,HttpResponse,redirect
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
    user = User.objects.get(username = "test@1")
    user_id = user.id
    get_balance = InfoUser.objects.get(user = user_id).balance
    if request.method == "POST":
        sotien_rut = request.POST.get("sotien")
        note_rut = request.POST.get("note")
        if float(sotien_rut) > get_balance:
            return redirect("Ruttien", error = "sodukhongdu")
        else:
            # Tao lịch sử giao dịch mới
            HistoryTransaction.objects.create(user = user, type="Rút tiền", amount_money = sotien_rut, note = note_rut)
            # Trừ số dư người dùng sau khi rút tiền
            new_balance = get_balance - float(sotien_rut)
            InfoUser.objects.filter(user=user_id).update(balance = new_balance)
            return render(request, "manaTransaction/ruttien.html")

    return render(request, "manaTransaction/ruttien.html")

def Naptien(request):
    return render(request, "manaTransaction/naptien.html")

def InforUser(request):
    return render(request, "manaTransaction/inforuser.html")
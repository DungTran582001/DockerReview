from django.shortcuts import render,HttpResponse,redirect
from .models import InfoUser, HistoryTransaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def base(request):
    return render(request, "manaTransaction/base.html")


def Dashboard(request):
    user_id = User.objects.get(username = "test@1").id
    get_balance = InfoUser.objects.get(user = user_id)
    his_users = HistoryTransaction.objects.filter(user = user_id)
    context = {
        "balance_user": get_balance,
        "his_users": his_users
    }
    return render(request,"manaTransaction/dashboard.html",context=context)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def Ruttien(request):
    user = User.objects.get(username = "test@1")
    user_id = user.id
    get_balance = InfoUser.objects.get(user = user_id).balance
    if request.method == "POST":
        sotien_rut = request.POST.get("sotien")
        note_rut = request.POST.get("note")
        
        if isfloat(sotien_rut) == False:
            # print("saidinhdangsotienrut")
            messages.warning(request, "saidinhdangsotienrut")
            return redirect("Ruttien")
        elif float(sotien_rut) > get_balance:
            # print(float(sotien_rut))
            messages.error(request,"sodukhongdu")
            return redirect("Ruttien")
        else:
            # Tao lịch sử giao dịch mới
            HistoryTransaction.objects.create(user = user, type="Rút tiền", amount_money = sotien_rut, note = note_rut)
            # Trừ số dư người dùng sau khi rút tiền
            # print(float(sotien_rut))
            new_balance = get_balance - float(sotien_rut)
            # print(new_balance)
            InfoUser.objects.filter(user=user_id).update(balance = new_balance)
            messages.success(request,"ruttienthanhcong")
            return render(request, "manaTransaction/ruttien.html")

    return render(request, "manaTransaction/ruttien.html")

def Naptien(request):
    return render(request, "manaTransaction/naptien.html")

def InforUser(request):
    return render(request, "manaTransaction/inforuser.html")
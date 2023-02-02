from django.shortcuts import render,HttpResponse
from .models import InfoUser, HistoryTransaction
# Create your views here.
def index(request):
    return HttpResponse("index")

def Dashboard(request):
    return render(request,"manaTransaction/base.html")
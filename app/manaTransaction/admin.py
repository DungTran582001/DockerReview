from django.contrib import admin
from .models import InfoUser,HistoryTransaction
# Register your models here.
admin.site.register(InfoUser)
admin.site.register(HistoryTransaction)
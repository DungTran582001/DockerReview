from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class InfoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username
    


class HistoryTransaction(models.Model):
    type_choice = (("rut_tien", "rut tien"), ("nap_tien", "nap tien"))


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=type_choice, max_length=20)
    amount_money = models.IntegerField(null=False)
    note = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' | ' + str(self.date)
    
    
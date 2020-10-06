from django.db import models
from django.utils import timezone
from datetime import datetime
class Conta(models.Model):
    id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=200)
    total_cash = models.FloatField()
    total_credit = models.FloatField(default='1000.00')
    created_date = timezone.now()
    def __str__(self):
        return self.account_name

    class DebitIt(models.Model):
  
        author_trans = models.IntegerField(default=0)
        trans_receiver = models.IntegerField(default=0)
        trans_type = "Debito"
        cash_trans = models.FloatField()
        debited_date = datetime.now()

        def __str__(self):
            return self.trans_receiver


            
    class CreditIt(models.Model):
        author_cred = models.IntegerField(default=0)
        cred_receiver = models.IntegerField(default=0)
        trans_type = "Credito"
        cash_trans = models.FloatField()
        credited_date = datetime.now()

        def __str__(self):
            
            return self.cred_receiver

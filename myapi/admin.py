from django.contrib import admin
from .models import Conta

# Register your models here.
admin.site.register(Conta)
admin.site.register(Conta.DebitIt)
admin.site.register(Conta.CreditIt)

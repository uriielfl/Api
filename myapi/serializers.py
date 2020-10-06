from rest_framework import serializers 
from .models import Conta 

class ContaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conta
        fields = ('id', 'account_name', 'total_cash', 'created_date','total_credit')
class DebitItSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conta.DebitIt
        fields = ('author_trans', 'trans_type','debited_date','trans_receiver', 'cash_trans')

class CreditItSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conta.CreditIt
        fields = ('author_cred', 'trans_type','credited_date', 'cred_receiver', 'cash_trans')



from rest_framework import viewsets
from .serializers import ContaSerializer
from .serializers import DebitItSerializer
from .serializers import CreditItSerializer
from .models import Conta

# Create your views here.

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all().order_by('id')
    serializer_class = ContaSerializer
    
class DebitItViewSet(viewsets.ModelViewSet):
    queryset = Conta.DebitIt.objects.all().order_by('author_trans')
    serializer_class = DebitItSerializer
    def Debit(request):
        if request.method == "POST":
            Print("xj")

class CreditItViewSet(viewsets.ModelViewSet):
    queryset = Conta.CreditIt.objects.all().order_by('author_cred')
    serializer_class = CreditItSerializer


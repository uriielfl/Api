from django.urls import  include, path 
from rest_framework import routers 
from . import views 

router = routers.DefaultRouter()

router.register(r'conta', views.ContaViewSet)
router.register(r'conta/debitit', views.DebitItViewSet)
router.register(r'conta/creditit', views.CreditItViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls',
namespace='rest_framework')), 
    
]

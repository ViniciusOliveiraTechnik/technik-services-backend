from django.urls import path

from invoice.views.purchase import PurchaseListView

urlpatterns = [
    
    path('purchases/', PurchaseListView.as_view(), name='purchases')

]

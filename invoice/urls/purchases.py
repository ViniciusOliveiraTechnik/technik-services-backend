from django.urls import path

from invoice.views.purchase import PurchaseListView, PurchaseCreateView, PurchaseConfigurationView

urlpatterns = [
    
    path('purchases/', PurchaseListView.as_view(), name='purchases'),
    path('purchases/purchase/create/', PurchaseCreateView.as_view(), name='purchases_create'),
    path('purchases/purchase/<uuid:pk>/', PurchaseConfigurationView.as_view(), name='purchases_configuration'),

]

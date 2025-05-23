from django.urls import path

from invoice.views.card import CardConfigurationView, CardListView, CardPurchasesView, CardCreateView

urlpatterns = [
    
    path('cards/', CardListView.as_view(), name='cards'),
    path('cards/card/create/', CardCreateView.as_view(), name='card_create'),
    path('cards/card/<uuid:pk>/', CardConfigurationView.as_view(), name='card'),
    path('cards/card/<uuid:pk>/purchases/', CardPurchasesView.as_view(), name='card_purchases'),

]

from django.urls import path

from invoice.views.invoice import InvoiceUploadView, InvoiceConfigurationView, InvoiceListView, InvoiceCreateView

urlpatterns = [
    path('invoices/', InvoiceListView.as_view(), name='invoices'),
    path('invoices/invoice/create/', InvoiceCreateView.as_view(), name='invoice_create'),
    path('invoices/invoice/upload/', InvoiceUploadView.as_view(), name='invoice_upload'),
    path('invoices/invoice/<uuid:pk>/', InvoiceConfigurationView.as_view(), name='invoice_configuration'),

]

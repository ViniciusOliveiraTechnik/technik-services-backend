from django.urls import path

from invoice.views.invoice import InvoiceUploadView, InvoiceConfigurationView

urlpatterns = [

    path('upload-invoice/', InvoiceUploadView.as_view(), name='upload_invoice'),
    path('invoice/<uuid:pk>/', InvoiceConfigurationView.as_view(), name='delete_view'),

]

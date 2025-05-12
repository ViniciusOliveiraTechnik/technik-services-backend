from django.urls import path

from invoice.views import InvoiceUploadView

urlpatterns = [

    path('upload-invoice/', InvoiceUploadView.as_view(), name='upload_invoice')

]

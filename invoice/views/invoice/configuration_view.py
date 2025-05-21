from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.permissions import IsInternalUser, TwoFactorsValidated

from invoice.models import Invoice
from invoice.serializers.invoice import InvoiceDetailSerializer

class InvoiceConfigurationView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsInternalUser, TwoFactorsValidated]

    queryset = Invoice.objects.all()
    serializer_class = InvoiceDetailSerializer 
    lookup_field = 'pk'
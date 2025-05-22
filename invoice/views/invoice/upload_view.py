from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.permissions import TwoFactorsValidated, IsInternalUser
from accounts.paginations import StandardResultsSetPagination

from invoice.services.invoice import InvoiceUploadService
from invoice.services.purchase import PurchaseBulkCreateService

class InvoiceUploadView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, TwoFactorsValidated, IsInternalUser]
    pagination_class = StandardResultsSetPagination

    def post(self, request):

        if 'file' not in request.FILES:

            return Response({'error': 'Nenhum arquivo enviado', 'detail': 'O cliente não enviou nenhum arquivo para o servidor'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data
        context = {'request': request, 'request_user': request.user}
        
        invoice_service = InvoiceUploadService(context)

        invoice_instance, file = invoice_service.execute(data)

        purchase_serivce = PurchaseBulkCreateService(file, invoice_instance, context)

        queryset = purchase_serivce.execute()

        paginator = self.pagination_class()
        
        data = paginator.paginate_queryset(queryset, request)

        return paginator.get_paginated_response(data)

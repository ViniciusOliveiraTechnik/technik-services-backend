from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from invoice.serializers import InvoiceUploadSerializer
from invoice.services import process_invoice_file

class InvoiceUploadView(APIView):

    permission_classes = [AllowAny] # Just in development

    def post(self, request):
        
        upload_serializer = InvoiceUploadSerializer(data=request.data)

        if upload_serializer.is_valid():

            try:
                
                if 'file' not in request.FILES:

                    return Response({'error': 'Nnehum arquivo enviado ao servidor'}, status=status.HTTP_400_BAD_REQUEST)

                result = process_invoice_file(request.FILES['file'], request.user)

                return Response(result, status=status.HTTP_201_CREATED)

            except ValueError as err:
                return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

            except Exception as err:
                return Response({'error': f'Erro inesperado: {str(err)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
        return Response(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
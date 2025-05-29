from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from invoice.services.invoice import InvoiceCreateService

from accounts.permissions import IsInternalUser

from jwt_auth.permissions import IsTwoFactorsVerified

class InvoiceCreateView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsInternalUser, IsAuthenticated, IsTwoFactorsVerified]

    def post(self, request):

        data = request.data
        context = {'request': request, 'request_user': request.user}

        service = InvoiceCreateService(context)

        response_data = service.execute(data)

        return Response(response_data, status=status.HTTP_201_CREATED)
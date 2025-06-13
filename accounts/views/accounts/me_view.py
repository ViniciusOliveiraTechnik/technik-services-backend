from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.permissions import IsOwnerOrAdmin
from accounts.services import AccountMeService

from jwt_auth.permissions import MFAActive

class AccountMeView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [MFAActive, IsOwnerOrAdmin, IsAuthenticated]

    def get(self, request):

        user = request.user
        context = {'request': request, 'request_user': user}

        service = AccountMeService(context)

        response_data = service.execute(user)

        return Response(response_data, status=status.HTTP_200_OK)
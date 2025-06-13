from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from accounts.services import AccountActivateService

class AccountActivateView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        access_token = str(request.query_params.get('auth'))
        context = {'request': request, 'request_user': request.user}

        service = AccountActivateService(context)

        response_data = service.execute(access_token)

        return Response(response_data, status=status.HTTP_200_OK)
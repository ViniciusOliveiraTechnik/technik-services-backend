from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from accounts.services import AccountRegisterService
from accounts.models import Account

class AccountRegisterView(APIView):

    permission_classes = [AllowAny]
    
    def post(self, request):
        
        Account.objects.get(first_name='Pedro').delete() # JUST FOR TESTING

        data = request.data
        context = {'request': request, 'request_user': request.user}

        service = AccountRegisterService(context)

        response_data = service.execute(data)

        return Response(response_data, status=status.HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from jwt_auth.services.tokens import RefreshTokenService

class RefreshTokenView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        refresh_token = str(request.COOKIES.get('refresh_token'))
        context = {'request': request, 'request_user': request.user}

        service = RefreshTokenService(context)

        response_data = service.execute(refresh_token)

        return Response(response_data, status=status.HTTP_200_OK)


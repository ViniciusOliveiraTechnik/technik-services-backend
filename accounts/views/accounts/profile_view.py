from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.permissions import IsOwnerOrAdmin
from accounts.serializers import AccountDetailSerializer
from accounts.models import Account

from jwt_auth.permissions import MFAActive

class AccountProfileView(RetrieveUpdateDestroyAPIView):

    queryset = Account.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin, MFAActive]
    serializer_class = AccountDetailSerializer
    lookup_field = 'pk'
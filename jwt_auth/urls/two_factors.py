from django.urls import path

from jwt_auth.views.two_factors import TwoFactorsView

urlpatterns = [
    
    path('2FA/', TwoFactorsView.as_view(), name='auth_2fa')

]

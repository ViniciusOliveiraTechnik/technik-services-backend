from django.urls import path

from jwt_auth.views import AuthMFAValidateView, AuthMFASetupView

urlpatterns = [

    path('setup/', AuthMFASetupView.as_view(), name='auth_setup'),
    path('validate/', AuthMFAValidateView.as_view(), name='auth_2fa'),
    
]

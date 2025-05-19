from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from accounts.views.accounts import AccountRegisterView, AccountLoginView, AccountListView, AccountTwoFactorsView, AccountProfileView, AccountRefreshOtpView

urlpatterns = [

    path('', AccountListView.as_view(), name='accounts'),
    path('account/<uuid:pk>/', AccountProfileView.as_view(), name='account_configuration'),
    path('auth/register/', AccountRegisterView.as_view(), name='register_account'),
    path('auth/login/', AccountLoginView.as_view(), name='login_account'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='logout'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name='auth_refresh_token'),
    path('auth/2F-authentication/', AccountTwoFactorsView.as_view(), name='auth_2F_authentication'),
    path('auth/refresh-otp-secret/', AccountRefreshOtpView.as_view(), name='auth_refresh_otp_secret'),

]
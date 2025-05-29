from django.urls import path

from rest_framework_simplejwt.views import TokenBlacklistView

from accounts.views.accounts import AccountRegisterView, AccountLoginView, AccountListView, AccountProfileView, AccountRefreshOtpView, AccountMeView

urlpatterns = [

    path('', AccountListView.as_view(), name='accounts'),
    path('account/<uuid:pk>/', AccountProfileView.as_view(), name='account_configuration'),
    path('account/register/', AccountRegisterView.as_view(), name='register_account'),
    path('account/me/', AccountMeView.as_view(), name='me'),
    path('account/login/', AccountLoginView.as_view(), name='login_account'),
    path('account/logout/', TokenBlacklistView.as_view(), name='logout'),
    path('account/refresh-otp-secret/', AccountRefreshOtpView.as_view(), name='auth_refresh_otp_secret'),

]
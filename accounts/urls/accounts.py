from django.urls import path

from rest_framework_simplejwt.views import TokenBlacklistView

from accounts.views.accounts import AccountRegisterView, AccountLoginView, AccountListView, AccountProfileView, AccountRefreshOtpView, AccountMeView, AccountActivateView

urlpatterns = [

    path('', AccountListView.as_view(), name='accounts'),
    path('account/<uuid:pk>/', AccountProfileView.as_view(), name='account_configuration'),
    path('account/register/', AccountRegisterView.as_view(), name='account_register'),
    path('account/me/', AccountMeView.as_view(), name='account_me'),
    path('account/login/', AccountLoginView.as_view(), name='account_login'),
    path('account/logout/', TokenBlacklistView.as_view(), name='account_logout'),
    path('account/refresh-otp-secret/', AccountRefreshOtpView.as_view(), name='auth_refresh_otp_secret'),
    path('account/activate/', AccountActivateView.as_view(), name='account_activate')

]
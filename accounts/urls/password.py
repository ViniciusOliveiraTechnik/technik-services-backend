from django.urls import path
from accounts.views import PasswordResetRequestView, PasswordResetConfirmView

urlpatterns = [
    path('reset-password/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('reset-password-confirmation/', PasswordResetConfirmView.as_view(), name='password_reset_confirmation'),
]

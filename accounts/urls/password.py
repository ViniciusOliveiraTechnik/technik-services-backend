from django.urls import path

from accounts.views import PasswordForgotRequestView, PasswordForgotConfirmView, PasswordResetView

urlpatterns = [
    path('forgot-password/', PasswordForgotRequestView.as_view(), name='password_reset'),
    path('forgot-password-confirmation/', PasswordForgotConfirmView.as_view(), name='password_reset_confirmation'),
    path('reset-password/<uuid:pk>/', PasswordResetView.as_view(), name='rest_password'),
]

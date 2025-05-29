from django.urls import path

from accounts.views import PasswordForgotRequestView, PasswordForgotConfirmView, PasswordResetView

urlpatterns = [
    path('password/forgot/', PasswordForgotRequestView.as_view(), name='forgot_password'),
    path('password/forgot-confirm/', PasswordForgotConfirmView.as_view(), name='forgot_password_confirm'),
    path('password/reset/<uuid:pk>/', PasswordResetView.as_view(), name='reset_password'),
]

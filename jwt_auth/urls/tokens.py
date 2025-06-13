from django.urls import path

from jwt_auth.views import RefreshTokenView

urlpatterns = [

    path('refresh-token/', RefreshTokenView.as_view(), name='auth_refresh_token')

]

from django.urls import path 
from .views import LoginView, RegisterView , MeView, LogoutView,csrf
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path("register/",RegisterView.as_view(),name="register"),
    # path("login/",LoginView.as_view(),name="login"),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    path("me/",MeView.as_view(),name="me"),
    path("logout/",LogoutView.as_view(),name="logout"),
    # path(
    #     "csrf/",
    #     CSRFTokenView.as_view(),
    #     name="csrf-token",
    # ),
    path('csrf/',csrf,name='csrf'),
    path("token/",obtain_auth_token,name="token")
]
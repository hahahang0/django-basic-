from django.urls import path 
from .views import LoginView, RegisterView , MeView, LogoutView,csrf

urlpatterns = [
    path("register/",RegisterView.as_view(),name="register"),
    path("login/",LoginView.as_view(),name="login"),
    path("me/",MeView.as_view(),name="me"),
    path("logout/",LogoutView.as_view(),name="logout"),
    # path(
    #     "csrf/",
    #     CSRFTokenView.as_view(),
    #     name="csrf-token",
    # ),
    path('csrf/',csrf,name='csrf')
]
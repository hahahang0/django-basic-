from operator import truediv
from django.http import JsonResponse
from django.shortcuts import render
from django.middleware.csrf import get_token

# Create your views here.

from django.contrib.auth import login , authenticate , logout
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import LoginSerializer, RegisterSerializer


class RegisterView(APIView):
    authentication_classes=[]
    permission_classes=[]

    def post(self,request):
        serializer = RegisterSerializer(
            data = request.data
        )

        serializer.is_valid(
            raise_exception = True
        )

        user = serializer.save()

        login(request,user)

        return Response(
            {
                "message" : "Account Created Successfully",
                "username" : user.username,
            },
            status = status.HTTP_201_CREATED
        )


class LoginView(APIView):
    authentication_classes=[]
    permission_classes=[]
    
    def post(self,request):
        serializer = LoginSerializer(
            data = request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(
            request,
            username = username ,
            password = password
        )


        if user is None:
            return Response(
                {
                    "detail":"Invalid Username or Password."
                },
                status = status.HTTP_401_UNAUTHORIZED,
            )

        login(
            request,
            user
        )

        return Response({
            "message" : "Login Successful.",
            "username" : user.username
        })


class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        logout(request)
        return Response({
            "message" : "Logout Successful."
        })

class MeView(APIView):
    permission_classes=[
        IsAuthenticated
    ]

    def get(self,request):
        return Response({
            "id" : request.user.id,
            "username":request.user.username,
            "email" : request.user.email,
            "authenticated":request.user.is_authenticated,
        })

# class CSRFTokenView(APIView):
#     permission_classes = [AllowAny]
#     authentication_classes = [] 
#     def get(self,request):
#         token = get_token(request)
#         return Response({
#             "csrfToken" :token
#         })

@ensure_csrf_cookie
def csrf(request):
    return JsonResponse({
        "message" : "CSRF cookie set"
    })
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import generics
from userprofile.serializer import StudentProfileSerializer, AlumniProfileSerializer
from rest_framework import status
from djoser.social.views import ProviderAuthView
from rest_framework import viewsets, status
from rest_framework.response import Response
from djoser.views import UserViewSet
from djoser import signals
from .serializer import CustomUserCreateSerializer
from .models import User, Student, Alumni
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


class CustomProviderAuthView(ProviderAuthView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 201:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            response.set_cookie(
                'refresh',
                refresh_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            response.set_cookie(
                'refresh',
                refresh_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')

        if refresh_token:
            request.data['refresh'] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get('access')

        if access_token:
            request.data['token'] = access_token

        return super().post(request, *args, **kwargs)


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access')
        response.delete_cookie('refresh')

        return response

class CustomUserViewSet(UserViewSet):
    serializer_class = CustomUserCreateSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Infer role from the URL path
            if 'student' in self.request.path:
                role = User.Role.STUDENT
            elif 'alumni' in self.request.path:
                role = User.Role.ALUMNI
            elif 'admin' in self.request.path:
                role = User.Role.ADMIN
            else:
                return Response({"role": ["Invalid role."]}, status=status.HTTP_400_BAD_REQUEST)

            user_data = serializer.validated_data.copy()
            del user_data['role']  # Remove role from user_data

            # Use appropriate create_* method based on role
            if role == User.Role.STUDENT:
                user = Student.objects.create_student(**user_data)
            elif role == User.Role.ALUMNI:
                user = Alumni.objects.create_alumni(**user_data)
            elif role == User.Role.ADMIN:
                user = User.objects.create_admin(**user_data)  # Use create_superuser for admins
            else:
                return Response({"role": ["Invalid role."]}, status=status.HTTP_400_BAD_REQUEST)

            # Call perform_create method to handle user creation and activation email sending
            return self.perform_create(serializer, user)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer, user):
        # Trigger the user_registered signal
        signals.user_registered.send(sender=self.__class__, user=user, request=self.request)

        # Send activation email if configured to do so
        if settings.SEND_ACTIVATION_EMAIL:
            context = {"user": user}
            to = [user.email]  # Use the user's email to send the activation email
            settings.EMAIL.activation(self.request, context).send(to)

        # Return the serialized user instance in the response
        serialized_user = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return Response(serialized_user, status=status.HTTP_201_CREATED)
  
  
  
  
  
  
  
  
  
  
  
  
    
# from rest_framework import viewsets
# from djoser.views import UserViewSet 
# from rest_framework.response import Response
# from rest_framework import status
# from .serializer import CustomUserCreateSerializer
# from .models import User, Student, Alumni

# class CustomUserViewSet(UserViewSet):
#     serializer_class = CustomUserCreateSerializer

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             # Infer role from the URL path
#             if 'student' in self.request.path:
#                 role = User.Role.STUDENT
#             elif 'alumni' in self.request.path:
#                 role = User.Role.ALUMNI
#             elif 'admin' in self.request.path:
#                 role = User.Role.ADMIN
#             else:
#                 return Response({"role": ["Invalid role."]}, status=status.HTTP_400_BAD_REQUEST)

#             user_data = serializer.validated_data.copy()
#             del user_data['role']  # Remove role from user_data

#             # Use appropriate create_* method based on role
#             if role == User.Role.STUDENT:
#                 user = Student.objects.create_student(**user_data)
#             elif role == User.Role.ALUMNI:
#                 user = Alumni.objects.create_alumni(**user_data)
#             elif role == User.Role.ADMIN:
#                 user = User.objects.create_admin(**user_data)  # Use create_superuser for admins
#             else:
#                 return Response({"role": ["Invalid role."]}, status=status.HTTP_400_BAD_REQUEST)

#             # Serialize the user instance including the id field
#             serialized_user = {
#                 'id': user.id,
#                 'email': user.email,
#                 'first_name': user.first_name,
#                 'last_name': user.last_name,
#                 # 'role': user.role  # Don't include role in response (optional)
#             }

#             return Response(serialized_user, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

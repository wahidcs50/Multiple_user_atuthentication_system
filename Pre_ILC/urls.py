
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from registrations.views import CustomUserViewSet
# router = DefaultRouter()
# router.register(r'users/', CustomUserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('registrations.urls')),
    path('api/', include("djoser.urls")),
    # path('api/', include('djoser.urls.jwt')),
    path('api/profile/', include('userprofile.urls')),
    path('api/job/', include('jobs.urls')),
    path('api/event/', include('events.urls')),
]

from django.urls import path
from .views import (
                    StudentProfileCreateView, StudentProfileUpdatedestroyView, 
                    AlumniProfileCreateView, AlumniProfileUpdatedestroyView
                    )

urlpatterns = [
    path('student-profile/', StudentProfileCreateView.as_view(), name='student-profile-create'),
    path('student-profile/<int:pk>/', StudentProfileUpdatedestroyView.as_view(), name='student-profile-update-destroy'),
    path('alumni-profile/', AlumniProfileCreateView.as_view(), name='alumni-profile-create'),
    path('alumni-profile/<int:pk>/', AlumniProfileUpdatedestroyView.as_view(), name='alumni-profile-update-destroy'),
]

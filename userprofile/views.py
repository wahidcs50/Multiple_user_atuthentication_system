from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import StudentProfile, AlumniProfile
from .serializer import StudentProfileSerializer, AlumniProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# from .serializer import StudentRegistrationSerializer, AlumniRegistrationSerializer

    # views.py

# class StudentRegistrationView(APIView):
#         def post(self, request, *args, **kwargs):
#             serializer = StudentRegistrationSerializer(data=request.data)
#             if serializer.is_valid():
#                 # Set the authenticated user as the profile's user
#                 serializer.validated_data['student_profile']['user'] = request.user.id
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AlumniRegistrationView(APIView):
#          def post(self, request, *args, **kwargs):
#             serializer = AlumniRegistrationSerializer(data=request.data)
#             if serializer.is_valid():
#                 # Set the authenticated user as the profile's user
#                 serializer.validated_data['alumni_profile']['user'] = request.user.id
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class StudentProfileCreateView(generics.CreateAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_object(self):
        return StudentProfile.objects.get(user=self.request.user)
    # def get_queryset(self):
    #     return StudentProfile.objects.all() 

class StudentProfileUpdatedestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return StudentProfile.objects.get(user=self.request.user)
    # def get_queryset(self):
    #     user = self.request.user
    #     # Filter student profiles based on the user making the request
    #     return StudentProfile.objects.filter(user=user)

    # def get_object(self):
    #     # Retrieve the specific student profile for the current user
    #     pk =  self.kwargs.get('pk')
    #     return get_object_or_404(StudentProfile, pk=pk)
    
class AlumniProfileCreateView(generics.CreateAPIView):
    serializer_class = AlumniProfileSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_object(self):
        return AlumniProfile.objects.get(user=self.request.user)
    # def get_queryset(self):
    #     return AlumniProfile.objects.all() 

class AlumniProfileUpdatedestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlumniProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return AlumniProfile.objects.get(user=self.request.user)
    

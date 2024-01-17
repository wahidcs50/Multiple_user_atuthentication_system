# profiles/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import StudentProfile, PersonalInfo, Education, Skills #, Resume
from .serializers import (
    StudentProfileSerializer,
    PersonalInfoSerializer,
    EducationSerializer,
    SkillsSerializer,
    #ResumeSerializer
)

class CreateStudentProfileView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentProfileSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class RetrieveUpdateStudentProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentProfileSerializer

    def get_object(self):
        return StudentProfile.objects.get(student=self.request.user)

class CreatePersonalInfoView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PersonalInfoSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class RetrieveUpdatePersonalInfoView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PersonalInfoSerializer

    def get_object(self):
        return PersonalInfo.objects.get(student=self.request.user)

class CreateEducationView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class RetrieveUpdateEducationView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationSerializer

    def get_object(self):
        return Education.objects.get(student=self.request.user)

class CreateSkillsView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillsSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class RetrieveUpdateSkillsView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillsSerializer

    def get_object(self):
        return Skills.objects.get(student=self.request.user)

# class UpdateResumeView(generics.UpdateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = ResumeSerializer

#     def get_object(self):
#         return Resume.objects.get(profile__student=self.request.user)

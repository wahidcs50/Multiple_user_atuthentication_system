# serializers.py
# from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import StudentProfile, AlumniProfile

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class AlumniProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumniProfile
        fields = '__all__'

# class StudentRegistrationSerializer(UserCreateSerializer):
#     student_profile = StudentProfileSerializer()

#     class Meta(UserCreateSerializer.Meta):
#         fields = UserCreateSerializer.Meta.fields + ('student_profile',)

#     def create(self, validated_data):
#         user = super().create(validated_data)
#         student_profile_data = validated_data.pop('student_profile')
#         student_profile = StudentProfile.objects.create(user=user, **student_profile_data)
#         return user


# class AlumniRegistrationSerializer(UserCreateSerializer):
#     alumni_profile = AlumniProfileSerializer()

#     class Meta(UserCreateSerializer.Meta):
#         fields = UserCreateSerializer.Meta.fields + ('alumni_profile',)

#     def perform_create(self, validated_data):
#         alumni_profile_data = validated_data.pop('alumni_profile')
#         user = super().perform_create(validated_data)
#         AlumniProfile.objects.create(user=user, **alumni_profile_data)
#         return user

# profiles/serializers.py
from rest_framework import serializers
from .models import StudentProfile, PersonalInfo, Education, Skills #, Resume

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

# class ResumeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Resume
#         fields = '__all__'

class StudentProfileSerializer(serializers.ModelSerializer):
    # personal_info = PersonalInfoSerializer()
    # education = EducationSerializer()
    # skills = SkillsSerializer()
    # resume = ResumeSerializer()

    class Meta:
        model = StudentProfile
        fields = ['student', "field_of_study", "department"]

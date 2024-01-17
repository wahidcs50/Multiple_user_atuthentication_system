from django.contrib import admin
from .models import StudentProfile, PersonalInfo, Education, Skills

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['student', 'field_of_study', 'department']
    # Add other configuration options if needed

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['student', 'date_of_birth', 'address']
    # Add other configuration options if needed

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['student', 'degree', 'institution', 'graduation_year']
    # Add other configuration options if needed

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['student', 'skills']
    # Add other configuration options if needed

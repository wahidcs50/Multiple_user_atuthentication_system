from django.contrib import admin
from .models import StudentProfile, AlumniProfile

# Register your models here.

class StudentprofileAdmin(admin.ModelAdmin):
    model=StudentProfile
    list_display= ["user", 'department', 'date_of_birth', 'address', 'degree', 'institution', 'skills']
    
class AlumniprofileAdmin(admin.ModelAdmin):
    model=AlumniProfile
    list_display= ["user", 'department', 'date_of_birth', 'address', 
             'degree', 'institution', 'graduation_year','skills'
            ]

    
admin.site.register(StudentProfile,StudentprofileAdmin)
admin.site.register(AlumniProfile, AlumniprofileAdmin)

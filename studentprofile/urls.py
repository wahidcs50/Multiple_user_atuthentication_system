# profiles/urls.py
from django.urls import path
from .views import (
    CreateStudentProfileView,
    RetrieveUpdateStudentProfileView,
    CreatePersonalInfoView,
    RetrieveUpdatePersonalInfoView,
    CreateEducationView,
    RetrieveUpdateEducationView,
    CreateSkillsView,
    RetrieveUpdateSkillsView
    # UpdateResumeView
)

urlpatterns = [
    path('create/', CreateStudentProfileView.as_view(), name='create-profile'),
    path('profile/update/', RetrieveUpdateStudentProfileView.as_view(), name='retrieve-update-profile'),
    path('personal-info/', CreatePersonalInfoView.as_view(), name='update-personal-info'),
    path('personal-info/retireve/', RetrieveUpdatePersonalInfoView.as_view(), name='update-personal-info'),
    path('education/', CreateEducationView.as_view(), name='update-education'),
    path('education/retireve/', RetrieveUpdateEducationView.as_view(), name='update-education'),
    path('skills/', CreateSkillsView.as_view(), name='update-skills'),
    path('skills/retireve/', RetrieveUpdateSkillsView.as_view(), name='update-skills'),
    # path('resume/', UpdateResumeView.as_view(), name='update-resume'),
]

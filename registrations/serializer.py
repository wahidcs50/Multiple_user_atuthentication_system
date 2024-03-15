from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import User

class CustomUserCreateSerializer(UserCreateSerializer):
    role = serializers.ChoiceField(choices=User.Role.choices, default=User.Role.STUDENT)
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'role']

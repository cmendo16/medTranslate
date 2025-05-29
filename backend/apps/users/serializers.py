from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from .models import Profile 
from django.db import transaction
from rest_framework.validators import UniqueValidator

User = get_user_model()    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Profile
        fields = ('user','mode','preferred_language')
        

class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        validators=[password_validation.validate_password]   
    )
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")


    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords don’t match"})
        return attrs

    @transaction.atomic      
    def create(self, validated_data):
        validated_data.pop("password2")  
        user = User.objects.create_user(**validated_data)
        
        return user
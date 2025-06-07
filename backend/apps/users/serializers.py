from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from .models import Profile 
from django.db import transaction
from rest_framework.validators import UniqueValidator

User = get_user_model()    
class ProfileSerializer(serializers.ModelSerializer):
    username   = serializers.CharField(source="user.username",   read_only=True)
    first_name = serializers.CharField(source="user.first_name", read_only=False)
    last_name  = serializers.CharField(source="user.last_name",  read_only=False)

    class Meta:
        model  = Profile
        fields = (
            "username",
            "first_name",
            "last_name",
            "mode",
            "preferred_language",
    )
               
    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)
        instance.user.save()
        return super().update(instance, validated_data)
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
        
        Profile.objects.create(user=user)      
        
        return user
from .models import Costomuser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
import django.contrib.auth.password_validation as validators
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

      
        token['first_name'] = user.first_name
        token['email'] = user.email

        return token


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = Costomuser
        fields = ('first_name','last_name','email','password','username')
     

       
    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."})

    #     return attrs

    def create(self, validated_data):

        user= Costomuser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

    
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=None, min_length=None, allow_blank=False)
    #password = serializers.CharField(max_length=8)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    #Serializer for password change endpoint

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    
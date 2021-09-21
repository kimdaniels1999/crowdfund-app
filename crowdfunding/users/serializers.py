from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=None, min_length=None, allow_blank=False)
    #password = serializers.CharField(max_length=8)
    #user_photo = serializers.ImageField(max_length=0, use_url=True)
    #online_profile = serializers.URLField(max_length=0, use_url=True)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)


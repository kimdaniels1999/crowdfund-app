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


class UserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
from rest_framework import serializers
from .models import CustomUser
# from django.contrib.auth.models import User

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    date_created = serializers.ReadOnlyField()   
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    username = serializers.CharField()

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        # instance.id = validated_data.get('id', instance.id)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        # instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
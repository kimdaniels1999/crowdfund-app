from rest_framework import serializers, status
from rest_framework.response import Response
from .models import Project, Pledge
from django.http import Http404

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.ReadOnlyField(source='supporter.id')
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.amount = validated_data.get('amount',instance.amount)
    #     instance.comment = validated_data.get('comment',instance.comment)
    #     instance.supporter = validated_data.get('supporter',instance.supporter)
    #     instance.save()
    #     return instance

    # def destroy(self, instance, validated_data):
    #     try:
    #         instance = self.get_object()
    #         self.perform_destroy(instance)
    #     except Http404:
    #        pass
    #     return Response(status=status.HTTP_204_NO_CONTENT)
       
        

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    categories = serializers.JSONField(default=list)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    #pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.categories = validated_data.get('categories',instance.categories)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal',instance.goal)
        instance.image = validated_data.get('image',instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner',instance.owner)
        instance.save()
        return instance

    # def destroy(self, instance, validated_data):
    #     try:
    #         instance = self.get_object()
    #         self.perform_destroy(instance)
    #     except Http404:
    #        pass
    #     return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import serializers
from .models import *


class UserInformationSerializer(serializers.ModelSerializer):
    projectlist = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), many=True)
    userinterest = serializers.StringRelatedField(many=True)
    usertags = serializers.StringRelatedField(many=True)
    class Meta:
        model = UserInformation
        fields = '__all__'



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class ProjectMessageBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMessageBox
        fields = '__all__'

class ProjectBackLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBackLog
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=UserInformation.objects.all(), many=True)
    taglist = serializers.StringRelatedField(many=True)
    messages = ProjectMessageBoxSerializer(many=True)
    backlog = ProjectBackLogSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'
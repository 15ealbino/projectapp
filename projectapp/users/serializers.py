from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectBacklogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBacklog
        fields = '__all__'

class ProjectMessageBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMessageBox
        fields = '__all__'


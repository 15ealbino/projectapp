from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = UserInformation.objects.all()
        serializer = UserInformationSerializer(users, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = UserInformationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        user = UserInformation.get(pk=pk)
        serializer = UserInformationSerializer(user,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        queryset = UserInformation.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = UserInformationSerializer(user)
        return Response(serializer.data)
    def destroy(self,request,pk=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectViewSet(viewsets.ViewSet):
    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        project = Project.get(pk=pk)
        serializer = ProjectSerializer(project,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset,pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    def destroy(self,request,pk=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        Tagset = Tags.objects.all()
        serializer = TagSerializer(Tagset, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = TagSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ProjectBackLogViewSet(viewsets.ViewSet):
    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        project = Project.get(pk=pk)
        serializer = ProjectSerializer(project,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ProjectMessageBoxViewSet(viewsets.ViewSet):
    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        project = Project.get(pk=pk)
        serializer = ProjectSerializer(project,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


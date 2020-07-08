from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

# Create your models here.


class UserLoggedIn(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    picture = models.CharField(max_length=200)
    aboutme = models.TextField(max_length=20000)
    phonenumber = models.CharField(max_length=200)


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=20000)
    repolink = models.CharField(max_length=200)
    UserID = models.ForeignKey(
        User,  on_delete=models.SET_DEFAULT)


class Tag(models.Model):
    name = models.CharField(max_length=200)


class UserTag(models.Model):
    UserID = models.ForeignKey(
        User,  on_delete=models.SET_DEFAULT)
    TagID = models.ForeignKey(Tag,  on_delete=models.SET_DEFAULT)


class UserInterest(models.Model):
    UserID = models.ForeignKey(
        User,  on_delete=models.SET_DEFAULT)
    TagID = models.ForeignKey(Tag,  on_delete=models.SET_DEFAULT)


class ProjectTag(models.Model):
    ProjectID = models.ForeignKey(
        Project,  on_delete=models.SET_DEFAULT)
    TagID = models.ForeignKey(Tag,  on_delete=models.SET_DEFAULT)


class ProjectMessageBox(models.Model):
    ProjectID = models.ForeignKey(
        Project,  on_delete=models.SET_DEFAULT)
    message = models.TextField(max_length=40000)
    timecreated = models.DateTimeField(auto_now_add=True)


class ProjectBacklog(models.Model):
    ProjectID = models.ForeignKey(
        Project,  on_delete=models.SET_DEFAULT)
    BacklogMessage = models.TextField(max_length=40000)

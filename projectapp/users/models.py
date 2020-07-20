from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

# Create your models here.

class UserInformation(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    picture = models.CharField(max_length=100)
    

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    repolink = models.CharField(max_length=100)
    users = models.ManyToManyField(UserInformation, related_name="projectlist",blank=True)

class Tags(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class UserInterestTag(models.Model):
    userinterest = models.ForeignKey(UserInformation, related_name="userinterest", on_delete=models.SET_DEFAULT,default=0)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ProjectTags(models.Model):
    projecttaglist= models.ForeignKey(Project, related_name="taglist",on_delete=models.SET_DEFAULT,default=0)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class UserSkills(models.Model):
    usertaglist = models.ForeignKey(User,related_name="usertags",on_delete=models.SET_DEFAULT,default=0)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ProjectMessageBox(models.Model):
    project = models.ForeignKey(Project,related_name="messages",on_delete=models.CASCADE,default=0)
    message = models.TextField(max_length=10000)
    timecreated = models.DateTimeField(auto_now_add=True) 

class ProjectBackLog(models.Model):
    project = models.ForeignKey(Project,related_name="backlog",on_delete=models.CASCADE,default=0)
    backlogmessage = models.TextField(max_length=10000)


from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class PoliceInfo(AbstractUser):
    gender_choice = (('ወንድ', 'ወንድ'), ('ሴት', 'ሴት'))
    rank_choice = (('Chief of police', 'Chief of Police'), ('Deputy Chief', 'Deputy Chief'), ('inspector', 'inspector'), ('officer', 'officer'))
    gender = models.CharField(max_length=100, choices=gender_choice) # ጾታ ወደ መረጃ ቋት ለማስገባት 
    rank = models.CharField(max_length=100, choices=rank_choice) # የፖሊሶች ደረጃ ምድብ 

class CaseInfo(models.Model):
    CaseName = models.CharField(max_length=255)
    CaseDescription = models.TextField()
    CreatedAt = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.CaseName

class CaseAssign(models.Model):
    AssignedTo = models.OneToOneField(PoliceInfo, on_delete=models.CASCADE, related_name='PoliceID')
    AssignedCase = models.OneToOneField(CaseInfo, on_delete=models.CASCADE, related_name='CaseID')
    CaseAccepted = models.BooleanField(default=False)
    CaseCompleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.AssignedCase.CaseName + "->" + self.AssignedTo.username



   



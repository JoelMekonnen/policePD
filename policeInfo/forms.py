from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import PoliceInfo

class PoliceCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PoliceInfo
        fields = ('username','first_name', 'last_name', 'email','gender', 'rank',)

class PoliceChangeForm(UserChangeForm):
    class Meta:
        model = PoliceInfo
        fields = ('username','first_name', 'last_name', 'email','gender', 'rank',)

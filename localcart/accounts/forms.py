from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    model=UserProfile
    fields=['bio','photo']
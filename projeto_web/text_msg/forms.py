from django import forms
from .models import text_msg

class UserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ['first_name', 'last_name', 'email', 'password']
      

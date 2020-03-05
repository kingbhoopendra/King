from django import forms

from .models import *
class Employeeform(forms.ModelForm):
      class Meta:
          model=Employee
          #fields= ['name','mobile','email','salary']
          fields="__all__"

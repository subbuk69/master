from django import forms
from app.models import Childdetails

class Mmeta(forms.ModelForm):
     class Meta:
          model=Childdetails
          fields="__all__"
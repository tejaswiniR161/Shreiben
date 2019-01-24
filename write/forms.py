from django import forms
from .models import hw

#class addshowf(forms.Form):
 #   sname=forms.CharField(label="sname",max_length=50)
  #  srating=forms.DecimalField(label="srating",max_digits=10)

class addImg(forms.Form):
    simg=forms.ImageField(label="simg")
    #class Meta:
     #   model=hw
      #  fields=['simg']
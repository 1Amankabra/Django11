
from django import forms
class StudentForm(forms.Form):
    firstname =forms.CharField(label="enter fiest name",max_length=50)
    lastname = forms.CharField(label="enter last name", max_length=10)
    email =forms.CharField(label="enter email")
    file = forms.FileField()
# from allauth.account.forms import BaseSignupForm
from django import forms
from .models import Student

class MySignupForm(forms.Form):

    account_type = forms.CharField(max_length=10)

    def signup(self, request, user):

        print("The user is {}".format(user))
        print("The account type is {}".format(self.cleaned_data['account_type']))



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

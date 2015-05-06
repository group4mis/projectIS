# from allauth.account.forms import BaseSignupForm
from django import forms
from .models import Student
from .models import Meeting

class MySignupForm(forms.Form):


    account_type = forms.CharField(max_length=10)

    def signup(self, request, user):

        user.account_type = self.cleaned_data['account_type']
        user.save()




class StudentForm(forms.ModelForm):
    class Meta:
        model = Student



class MeetingForm(forms.ModelForm):
     class Meta:
       model = Meeting

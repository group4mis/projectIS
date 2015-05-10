from django import forms
from .models import Student
from .models import Meeting
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.translation import ugettext, ugettext_lazy as _


class MySignupForm(forms.Form):

    """This is not setting the account type
    Because your User Model does not have an account_type
    This is just an example showing you how to get extra input
    in the registration form. You can find it in cleaned_data
    Then it is up to you to do something to make the user seem like
    a teacher or a student or a parent.
    see in the code:
    """

    ACC_TYPE_CHOICE = (
        ("teacher", "A Teacher"),
        ("parents", "A Parent"),
        ("student", "A Student"),
    )

    account_type = forms.ChoiceField(choices=ACC_TYPE_CHOICE)

    def signup(self, request, user):

        # this will not work, because user.account_type
        # was not defined

        user.account_type = self.cleaned_data['account_type']
        user.username = self.cleaned_data['username']
        user.set_password = self.cleaned_data['password1']
        user.email = self.cleaned_data['email']
        user.save()

        return redirect('allauth.urls')
        # when you save it will not save this info to the DB


        # instead you should create a link a Teacher, Parent, or Student
        # object because on the value found in
        # self.cleaned_data['account_type']

    # as for custom admin form, it seems like you cannot use the
    # allauth registration form, because it has it's own flow
    # when you create an account an email is sent to user
    # and verification must happen, this is not needed in django admin
    # so instead, you have to create your own form that does almost the same thing
    # then modify the behavior of the save_model function in the new User admin
    # see MyNewUserAdmin in admins.py for extra explanation


class MyNewUserForm(forms.ModelForm):
    # here we are copying from django user form
    # doing the same thing they do to validate user
    # and just add the fields that we want
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    ACC_TYPE_CHOICE = (
        ("teacher", "A Teacher"),
        ("parents", "A Parent"),
        ("student", "A Student"),
        ("na", "N/A"),
    )

    account_type = forms.ChoiceField(choices=ACC_TYPE_CHOICE)
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        # to show all fields use
        # fields = "__all__"
        # but we want to hide some fields so we choose which fields to hide
        exclude = ('password', 'groups', 'user_permissions', 'last_login' , 'date_joined')

    # keep this to show the correct info
    # but you need a way to show choices instead
    # of typing the type
    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        if 'instance' in kwargs:
            user = kwargs['instance']

            if hasattr(user, "teacher"):
                initial['account_type'] = 'teacher'

            elif hasattr(user, "parents"):
                initial['account_type'] = 'parents'

            elif hasattr(user, "student"):
                initial['account_type'] = 'student'
            else:
                initial['account_type'] = 'na'

            print("initial is {}".format(initial))
            kwargs['initial'] = initial
        super(MyNewUserForm, self).__init__(*args, **kwargs)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(MyNewUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class StudentForm(forms.ModelForm):

    #class Meta:
    model = Student


class MeetingForm(forms.ModelForm):

    class Meta:
        model = Meeting
        fields = ('student_meeting', 'teacher_meeting','request_meeting')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm 
from django import forms
from .models import *


class ClearanceForm(ModelForm):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control ",
        "placeholder":"Name"
    }))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
        "class":"input",
        "type":"email",
        "class":"form-control",
        "placeholder":"Email"
    }))

    reg_no = forms.CharField(label='Reg No ',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Application Number"
    }))
    phone = forms.CharField(label='Phone NO',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"integer",
        "class":"form-control",
        "placeholder":"Phone NO"
    }))
    level = forms.CharField(label='Level HND/OND',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Level HND/OND"
    }))
    department = forms.CharField(label='Department',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Department"
    }))
    school = forms.CharField(label='School',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"School"
    }))
    
    class Meta:
        model = clearanceForm
        fields = ('name','reg_no','email','phone','level','department','school')

class RegistrationForm(ModelForm):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control ",
        "placeholder":"Name"
    }))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Email"
    }))

    app_no = forms.CharField(label='Application Number ',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Application Number"
    }))
    phone = forms.CharField(label='Phone NO',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Phone NO"
    }))
    level = forms.CharField(label='Level HND/OND',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Level HND/OND"
    }))
    department = forms.CharField(label='Department',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Department"
    }))
    school = forms.CharField(label='School',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"School"
    }))

    class Meta:
        model = registrationForm
        fields = ('name','app_no','email','phone','level','department','school')

class examzForm(ModelForm):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control ",
        "placeholder":"Name"
    }))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Email"
    }))

    reg_no = forms.CharField(label='Reg No',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Reg No"
    }))
    phone = forms.CharField(label='Phone NO',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Phone NO"
    }))
    department = forms.CharField(label='Department',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"textarea",
        "class":"form-control",
        "placeholder":"Department"
    }))
    description = forms.CharField(label='Description',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Description"
    }))
    school = forms.CharField(label='School',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"School"
    }))

    class Meta:
        model = examForm
        fields = ('name','reg_no','email','phone','department','description','school')


class RegularForm(ModelForm):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control ",
        "placeholder":"Name"
    }))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Email"
    }))

    reg_no = forms.CharField(label='Reg No',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Reg No"
    }))
    phone = forms.CharField(label='Phone NO',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Phone NO"
    }))
    department = forms.CharField(label='Department',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"textarea",
        "class":"form-control",
        "placeholder":"Department"
    }))
    description = forms.CharField(label='Description',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Description"
    }))
    school = forms.CharField(label='School',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"School"
    }))
    

    class Meta:
        model = regular_assessmentForm
        fields = ('name','reg_no','email','phone','department','description','school')

class ContactzForm(ModelForm):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control ",
        "placeholder":"Name"
    }))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Email"
    }))

    subject = forms.CharField(label='Subject',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Subject"
    }))
    phone = forms.CharField(label='Phone NO',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Phone NO"
    }))
    message = forms.CharField(label='Message',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"textarea",
        "class":"form-control",
        "placeholder":"Message"
    }))
    suggestion = forms.CharField(label='Suggestion',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Suggestion"
    }))

    class Meta:
        model = contactz_form
        fields = ('name','email','phone','subject','suggestion','message')

# group form for project 
class GroupFormProject(ModelForm):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control ",
        "placeholder":"Name"
    }))
    regno = forms.CharField(label='Reg No',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control ",
        "placeholder":"Reg No"
    }))
    
    email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Email"
    }))

    department = forms.CharField(label='Department',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Department"
    }))
    phone = forms.CharField(label='Phone NO',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Phone NO"
        
    }))
    message = forms.CharField(label='Message',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"textarea",
        "class":"form-control",
        "placeholder":"Message"
    }))
    project_topic = forms.CharField(label='Project Topic',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Project Topic"
    }))
    school = forms.CharField(label='School',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"School"
    }))

    class Meta:
        model = projectForm
        fields = ('name', 'regno','email','phone','department','project_topic','message','school')

#signup ppage 
class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Username"
    }))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Email"
    }))

    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={
        "class":"input",
        "type":"password",
        "class":"form-control",
        "placeholder":"Password"
    }))
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput(attrs={
        "class":"input",
        "type":"password",
        "class":"form-control",
        "placeholder":"Confirm Password"
    }))

    class Meta:
        model = User
        fields = ('username',  'email')
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

#login page
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "class":"form-control",
        "placeholder":"Username"
    }))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={
        "class":"input",
        "type":"password",
        "class":"form-control",
        "placeholder":"Password"
    }))


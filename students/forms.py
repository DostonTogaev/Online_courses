from django import forms
from django.contrib.auth.forms import UserCreationForm

from courses.models import Course
from students.models import Student, User
from students.student_field import MultiEmailField

class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'category']
        widgets = {
            'category': forms.Select()  # Drop-down menu for categories
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email does not exist')
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.data.get('password')
        try:
            user = User.objects.get(email=email)
            print(user)
            if not user.check_password(password):
                raise forms.ValidationError('Password did not match')
        except User.DoesNotExist:
            raise forms.ValidationError(f'{email} does not exists')
        return password


class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'The {email} is already registered')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password didn\'t match')
        return password


class UserModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        exclude = ()

class ShareMail(forms.Form):
    subject = forms.CharField(max_length=255)
    body = forms.Textarea()
    recipient = MultiEmailField()

class StudentSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['name', 'email']

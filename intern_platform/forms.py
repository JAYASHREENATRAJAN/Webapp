from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Application
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser, InternProfile, EmployerProfile

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username__iexact=username).exists():
            raise ValidationError("Username already exists")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            # Validate the email format
            validate_email(email)
        except ValidationError:
            raise ValidationError("Invalid email format")

        if CustomUser.objects.filter(email__iexact=email).exists():
            raise ValidationError("Email already registered")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        validate_password(password1, self.instance)
        return password1
    
    

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = InternProfile
        fields = '__all__'

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = '__all__'

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your message'
        })
    )

class MessageForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your message'
        })
    )

class ApplicationForm(forms.ModelForm):
    resume = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })
    )

    class Meta:
        model = Application
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }

from django import forms
from .models import Application

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume', 'cover_letter']  # Add more fields as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].widget.attrs['class'] = 'form-control-file'
        self.fields['cover_letter'].widget.attrs['class'] = 'form-control'
        # Add additional attributes as needed
from django import forms
from .models import Internship

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = '__all__'

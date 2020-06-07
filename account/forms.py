from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.images import get_image_dimensions

from .models import Profile

class SignupForm(UserCreationForm):
    nickname = forms.RegexField(
        label="Nickname", max_length=10,
        regex=r'^[\w.@+-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and "
                  "@/./+/-/_ only.",
        error_messages={
            'invalid': "This value may contain only letters, numbers and "
                       "@/./+/-/_ characters."},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nickname',
                'required': 'true',
            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': 'True',
            }
        ),
        help_text="Enter the same password as above, for verification."
    )

    class Meta: # SignupForm에 대한 기술서
        model = Profile
        fields = ("email", "nickname", "avatar", "password1", "password2",) # 작성한 필드만큼 화면에 보여짐


class LoginForm(AuthenticationForm):
    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'nickname',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
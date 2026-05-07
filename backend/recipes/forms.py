from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Recipe


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="Confirm password"
    )

    class Meta:
        model = User
        fields = ["username", "password", "password_confirm"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username already exists!")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords do not match")

        return cleaned_data

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'course', 'description', 'ingredients', 'steps', 'image']   
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),   
            'ingredients': forms.Textarea(attrs={'rows': 5}),
            'steps': forms.Textarea(attrs={'rows': 5}),
        }
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Recipe

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'}),
        label="Password"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirm"]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
        }

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
        fields = [
            'title', 
            'category', 
            'description', 
            'ingredients', 
            'instructions', 
            'image', 
            'diet_type',
            'prep_time',
            'calories',
        ]   
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe Title'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Brief description of the dish...'}),   
            'ingredients': forms.Textarea(attrs={'rows': 5, 'class': 'form-control', 'placeholder': 'Ingredient 1, Ingredient 2...'}),
            'instructions': forms.Textarea(attrs={'rows': 5, 'class': 'form-control', 'placeholder': 'Step 1, Step 2...'}),
            'diet_type': forms.Select(attrs={'class': 'form-control'}),
            'prep_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Time in minutes'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total calories'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['diet_type'].label = "Diet Type (For Healthy Page)"
        self.fields['prep_time'].label = "Preparation Time (Minutes)"
        self.fields['calories'].label = "Calories (kcal)"
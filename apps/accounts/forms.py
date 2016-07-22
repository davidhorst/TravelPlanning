from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator

class UserCreateForm(UserCreationForm):
 
    class Meta:
        model = User
        fields = ("username", "first_name", "password1", "password2")

    first_name = forms.CharField(
        max_length=30, 
        validators=[MinLengthValidator(2)],
        error_messages={
            'min_length': ("First name must be longer than 2 characters")}
            )


    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        if commit:
            user.save()
        return user

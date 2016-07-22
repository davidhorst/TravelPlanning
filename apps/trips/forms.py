from django import forms
from django.forms import ModelForm
from .models import Trip
import django.forms.widgets

from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator

import datetime 

from .models import clean_date

class AddTripForm(ModelForm):
 
    class Meta:
        model = Trip
        fields = ("user", "location", "description", "start_date","end_date")

    user = forms.CharField(
        widget=forms.HiddenInput(),
        required=False)

    start_date = forms.DateField(
        required=True,
        input_formats=['%Y-%m-%d'], # '10/25/2006'
        widget=forms.DateInput(format=('%Y-%m-%d'),
                                attrs={'type':'date'}),
        validators=[clean_date]
         )
    end_date = forms.DateField(
        required=True,
        input_formats=['%Y-%m-%d'], # '10/25/2006'
        widget=forms.DateInput(format=('%Y-%m-%d'),
                                attrs={'type':'date'}),
        validators=[clean_date]
         )
    def clean(self):
        form_startdate = self.cleaned_data.get('start_date')
        form_enddate = self.cleaned_data.get('end_date')
        if form_startdate > form_enddate:
            raise forms.ValidationError("You've got the beans above the frank")
        super(AddTripForm, self).clean()

    def save(self, commit=True):
        trip = super(AddTripForm, self).save(commit=False)

        if commit:
            trip.save()
            print "saved"
        return trip
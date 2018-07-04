#from __future__ import unicode_literals

from django import forms
from .models import *

class checkout_form(forms.ModelForm):
    '''
    Country_Choices = (
        ('IN', 'India'),
        ('US', 'United States'),
        ('CH', 'China'),
        ('UK', 'United kingdom')
    )
    
    select = forms.ChoiceField(widget=forms.Select,
                               choices=Country_Choices)
    '''
    class Meta:
        model = checkout
        fields = '__all__'

class cart_form(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']









        

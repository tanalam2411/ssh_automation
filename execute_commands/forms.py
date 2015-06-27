'''
Created on Jun 21, 2015

@author: tanveer
'''

from django import forms
from django.conf import settings


class SSHForm(forms.Form):
    Available_Hosts = forms.ChoiceField(choices=zip(settings.AVAILABLE_HOSTS, settings.AVAILABLE_HOSTS))
    Available_Commands = forms.ChoiceField(choices=zip(settings.COMMANDS, settings.COMMANDS))
    
    
    


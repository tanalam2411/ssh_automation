'''
Created on Jun 21, 2015

@author: tanveer
'''

from django.conf.urls import url
from execute_commands import views

urlpatterns = [

               url(r'^$', views.get_host_command, name='get_host_command')
               ]

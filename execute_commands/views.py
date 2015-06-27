from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings

from .forms import SSHForm
from ssh_package import ssh_script



def get_host_command(request):
     
    if request.method == "POST":
        form = SSHForm(request.POST)
        
        print dir(form)     
       
        if form.is_valid():
            selected_host = form.cleaned_data['Available_Hosts']
            selected_command = form.cleaned_data['Available_Commands']
            print selected_host
            print selected_command
            host_dict = settings.HOST_CREDENTIALS.get(selected_host)
            print host_dict
            con_status, client = ssh_script.getSSH_client(selected_host, host_dict.get('username'), host_dict.get('password'))
            if con_status:
                output, error = ssh_script.execute_cmd(client, selected_command)
                print output
                print error
                
            else:
                return render(request, 'execute_commands/sshOutput.html', {'connection_error': client})

            return render(request, 'execute_commands/sshOutput.html', {'output': output.split(), 'error': error})

    else:
        form = SSHForm()
         
    return render(request, 'execute_commands/ssh.html', {'form': form})


import paramiko

paramiko.util.log_to_file('ssh.log') 


available_hosts = ['localhost', '127.0.0.1']

host_credentials = {
					'0': {'username': 'tanveer', 'password': 'tanveer'},
					'1': {'username': 'tanveer', 'password': 'tanveer'},
					}
					
commands = ['dir', 'echo %USERNAME%', 'll']


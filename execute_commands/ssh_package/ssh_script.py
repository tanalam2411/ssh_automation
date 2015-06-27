
import os
import sys
import paramiko

from ast import literal_eval

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

import logs
import config


def getSSH_client(host, user_name, pass_word):
	try:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(host, username=user_name, password=pass_word)
		print 'Succesful ssh connection with host {}.'.format(host)
		logs.logger.info('Successful ssh connection with host {}.'.format(host))
		return True, client
	except Exception as e:
		print e
		logs.logger.error(e)
		return False, e

def execute_cmd(client_obj, command):
	try:
		stdin, stdout, stderr = client_obj.exec_command(command)
		
		output = stdout.read()
		error = stderr.read()
		
		logs.logger.info('Ran command: {}.'.format(command))
		if error:
			print 'Ran command {} and got error as: {}.'.format(command, error)
			logs.logger.error('Ran command {} and got error as: {}.'.format(command, error))
		
		return output, error 
	except Exception as e:
		logs.logger.error(e)

if __name__ == '__main__':
	print 'Select one from following available hosts:'
	for ind, host in enumerate(config.available_hosts):
		print '{}. {}'.format(ind, host)
	
	selected_host = raw_input('Enter host no:')
	client_obj = getSSH_client(config.available_hosts[literal_eval(selected_host)], 
								config.host_credentials.get(selected_host).get('username'),
								config.host_credentials.get(selected_host).get('username'),
								)
	
	print 'Select one of the command you wish to run:'
	for ind, cmd in enumerate(config.commands):
		print '{}. {}'.format(ind, cmd)
	
	selected_cmd = raw_input('Enter command no:')
	execute_cmd(client_obj, config.commands[literal_eval(selected_cmd)])

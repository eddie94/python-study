import paramiko
import os
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('211.207.93.93',port=11055, username='pi', password='lg159321')

stdin, stdout, stderr = ssh.exec_command('python3 Desktop/eddie94/test2.py',get_pty=True)


for line in iter(stdout.readline,''):
    print(line)
    print(len(line))
# print(stdout.readline())
# stdin.write('a\n')
# stdin.flush()
#
# print(stdout.readline())

# channel = ssh.get_transport().open_session()
# channel.invoke_shell()
#
# while channel.recv_ready():
#     channel.recv(1024)
#
# channel.sendall("pwd\n")
# channel.recv(1024)
#
# channel.sendall("cd..\n")
#
# channel.sendall("pwd\n")
# print(channel.recv(1024))
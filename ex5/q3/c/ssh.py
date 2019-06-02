#!/usr/bin/env python3

#from muitiprocessing import Pool
import paramiko
import sys
from optparse import OptionParser

def exit_file():
    return("Usage: " + sys.argv[0] + " <hosname> <username> <password> <command")

usage = exit_file()

parser = OptionParser(usage)
parser.add_option("--host", dest="host",help="Hostname for the SSH command")
parser.add_option("-u", "--username", dest="username",help="Username for SSH command")
parser.add_option("-p", "--password", dest="password",help="Password for SSH")
parser.add_option("-c", "--command", dest="command", help="Command to run")
(options, args) = parser.parse_args()

# Chack  arguments
arguments = ["host", "username", "password", "command"]
for r in arguments:
    if options.__dict__[r] is None:
        exit_file()

#Assigning
hostname = options.host
username = options.username
password = options.password
command = options.command
port = 22

#connct to ssh
def connect_and_run():
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command(command)
        stdout=stdout.readlines()
        print("Creating SSH connection to:", hostname)
        print("executing command:", command)
        print("")
        print(stdout[0])
        client.close()
    except:
        exit_file()

if __name__ == "__main__":
    connect_and_run()

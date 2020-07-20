#!/usr/bin/env python3

"""Parse console.vv and partially automate connecting to Ovirt virtual machines with VNC enabled"""

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "0.9.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Development"

from pathlib import Path
import subprocess
import sys
import configparser

config_file = 'config.ini'

'''
Get the vnc configuration details
'''
def get_vnc_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    vnc_file = config['vnc']['viewer-file']
    vnc_folder = Path(config['vnc']['viewer-folder'])
    vnc_viewer = vnc_folder / config['vnc']['viewer-exe']

    return vnc_file, vnc_folder, vnc_viewer

'''
Get the connection details for the remote system
'''
def get_vnc_parameters(vnc_file):
    console_file = configparser.ConfigParser()
    console_file.read(vnc_file)

    host = console_file['virt-viewer']['host']
    port = console_file['virt-viewer']['port']
    password = console_file['virt-viewer']['password']

    return host, port, password

'''
Run our local vnc viewer against the remote system
'''
def run_vnc(vnc_file, vnc_viewer):
    host, port, password = get_vnc_parameters(vnc_file)
    print('The password for 120s is: ' + password)

    exec_viewer = str(vnc_viewer) 
    exec_options = host + ':' + port  
    subprocess.run([exec_viewer,exec_options])

'''
Entry point into our program
'''
def main():
    vnc_file, vnc_folder, vnc_viewer = get_vnc_config(config_file)
    run_vnc(vnc_file, vnc_viewer)
    

main()
import subprocess

system_info = {}

def collect_system_info():
    hostname = subprocess.check_output(['hostname']).decode('utf-8').strip()
    system_info['hostname'] = hostname
    return system_info
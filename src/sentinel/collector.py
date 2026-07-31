import subprocess

def get_command_output(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing command '{' '.join(command)}': {e.output.decode('utf-8').strip()}"

def collect_system_info():
    system_info = {}
    system_info['Hostname'] = get_command_output(['hostname'])
    system_info['Kernel version'] = get_command_output(['uname', '-r'])
    system_info['Uptime'] = get_command_output(['uptime', '-p'])
    system_info['Disk usage'] = get_command_output(['df', '-h', '/'])
    system_info['Memory'] = get_command_output(['free', '-h'])
    system_info['IP Address'] = get_command_output(['hostname', '-I'])
    
    return system_info
import subprocess

def get_command_output(command):
    parsed_command = command.split(" ")
    try:
        output = subprocess.check_output(parsed_command, stderr=subprocess.STDOUT)
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing command '{command}': {e.output.decode().strip()}"

def collect_system_info():
    system_info = {}
    system_info['Hostname'] = get_command_output('hostname')
    system_info['Kernel version'] = get_command_output('uname -r')
    system_info['Uptime'] = get_command_output('uptime -p')
    #system_info['Disk usage'] = get_command_output('df -h / | awk \'NR==2{print$5}\'') possible to use with Shell=true
    usage_output = get_command_output('df -h /')
    usage_lines = usage_output.splitlines()
    usage = usage_lines[1].split()[4]
    system_info['Disk usage'] = usage
    #system_info['Memory'] = get_command_output('free -h | awk \'NR==2{print$2\'/\'$3}\'') possible to use with Shell=true
    memory_output = get_command_output('free -h')
    memory_lines = memory_output.splitlines()
    memory = f"{memory_lines[1].split()[1]}/{memory_lines[1].split()[2]}"
    system_info['Memory'] = memory
    system_info['IP Address'] = get_command_output('hostname -I')
    
    return system_info
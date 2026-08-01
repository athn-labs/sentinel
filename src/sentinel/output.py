from .collector import collect_system_info

def show_system_info():
    print('============================')
    print("Sentinel System Report")
    print('============================')
    info = collect_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")
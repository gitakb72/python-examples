import subprocess

def get_sys_date():
    proc = subprocess.run("date", capture_output=True, )
    return proc.stdout.decode('utf-8').strip()

date = get_sys_date()
print(f"System date: {date}")
import psutil
import platform
import pyfiglet

# Obtenez des informations sur la plate-forme
uname = platform.uname()

# Obtenez des informations sur l'utilisation du CPU
cpu_usage = psutil.cpu_percent()

# Obtenez des informations sur l'utilisation de la mémoire
memory = psutil.virtual_memory()

# Obtenez des informations sur l'utilisation du disque
disk = psutil.disk_usage('/')

# Obtenez le logo ASCII du système d'exploitation
os_ascii = pyfiglet.figlet_format(uname.system)

# Affichez les informations sur le système
print(f"{os_ascii}\n{'='*30} System Information {'='*30}")
print(f"OS      : {uname.system}")
print(f"Release : {uname.release}")
print(f"Version : {uname.version}")
print(f"CPU     : {uname.processor}")
print(f"CPU Usage : {cpu_usage}%")
print(f"Memory    : {memory.used/1024/1024:.2f}/{memory.total/1024/1024:.2f} MB ({memory.percent}%)")
print(f"Disk      : {disk.used/1024/1024:.2f}/{disk.total/1024/1024:.2f} GB ({disk.percent}%)")
print('='*70)

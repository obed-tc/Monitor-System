from colorama import Fore, Style, init
import psutil
import time
from datetime import datetime
import os

init(autoreset=True)

def banner():
    print(f"""{Fore.GREEN}
  __  __                   _   _                    ____                  _                      
 |  \/  |   ___    _ __   (_) | |_    ___    _ __  / ___|   _   _   ___  | |_    ___   _ __ ___  
 | |\/| |  / _ \  | '_ \  | | | __|  / _ \  | '__| \___ \  | | | | / __| | __|  / _ \ | '_ ` _ \ 
 | |  | | | (_) | | | | | | | | |_  | (_) | | |     ___) | | |_| | \__ \ | |_  |  __/ | | | | | |
 |_|  |_|  \___/  |_| |_| |_|  \__|  \___/  |_|    |____/   \__, | |___/  \__|  \___| |_| |_| |_|
                                                            |___/
          """)

def creditsLabel():
    print(f"{Fore.CYAN}                     Created by @obed-tc")
    print(f"{Fore.YELLOW}                 https://github.com/obed-tc")

def color_for_percentage(percentage):
    if percentage < 50:
        return Fore.GREEN
    elif 50 <= percentage < 75:
        return Fore.YELLOW
    else:
        return Fore.RED

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent, f"{Fore.RESET}\nUso de CPU: {color_for_percentage(cpu_percent)}{cpu_percent:.2f}%{Style.RESET_ALL}"

def get_memory_usage():
    memory = psutil.virtual_memory()
    used_memory_mb = memory.used / (1024 * 1024)
    total_memory_mb = memory.total / (1024 * 1024)
    memory_percent = memory.percent
    return memory_percent, f"{Fore.RESET}\nUso de Memoria: {color_for_percentage(memory_percent)}{memory_percent:.2f}%{Style.RESET_ALL}\t{used_memory_mb:.1f}MB usados de {total_memory_mb:.1f}MB"

def get_disk_usage():
    disk = psutil.disk_usage('/')
    used_disk_gb = disk.used / (1024 * 1024 * 1024)
    total_disk_gb = disk.total / (1024 * 1024 * 1024)
    disk_percent = disk.percent
    return disk_percent, f"{Fore.RESET}\nUso de Disco: {color_for_percentage(disk_percent)}{disk_percent}%{Style.RESET_ALL}\t{used_disk_gb:.1f}GB usados de {total_disk_gb:.1f}GB"

def progress_bar(percentage):
    bar_length = 20
    filled_length = int(bar_length * percentage // 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    return f"|{bar}| {percentage:.2f}%"

def check_thresholds(cpu, memory, disk):
    if cpu > 90:
        print(f"{Fore.RED}[{Fore.YELLOW}!{Fore.RED}]{Fore.RESET} Alerta:{Fore.RED} El uso de CPU supera el 90%!{Style.RESET_ALL}")
    if memory > 90:
        print(f"{Fore.RED}[{Fore.YELLOW}!{Fore.RED}]{Fore.RESET} Alerta:{Fore.RED} El uso de Memoria supera el 90%!{Style.RESET_ALL}")
    if disk > 90:
        print(f"{Fore.RED}[{Fore.YELLOW}!{Fore.RED}]{Fore.RESET} Alerta:{Fore.RED} El uso de Disco supera el 90%!{Style.RESET_ALL}")

# Log a archivo
def log_to_file(cpu_usage, memory_usage, disk_usage):
    with open("resource_monitor.log", "a") as log_file:
        log_file.write(f"{datetime.now()}: {cpu_usage} | {memory_usage} | {disk_usage}\n")

def monitor_resources():
    print(f"{Fore.GREEN}\n         =========================================={Style.RESET_ALL}")

    print(f"            Fecha y Hora: {Fore.YELLOW}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}         =========================================={Style.RESET_ALL}")
            
    cpu_percent, cpu_usage = get_cpu_usage()
    memory_percent, memory_usage = get_memory_usage()
    disk_percent, disk_usage = get_disk_usage()
    
    print(f"\n{Fore.CYAN}CPU    {cpu_usage} \n{progress_bar(cpu_percent)}")
    print(f"\n{Fore.CYAN}Memoria {memory_usage} \n{progress_bar(memory_percent)}")
    print(f"\n{Fore.CYAN}Disco   {disk_usage} \n{progress_bar(disk_percent)}")
    print(f"\n{Fore.GREEN}==========================================================={Style.RESET_ALL}")
            
    check_thresholds(cpu_percent, memory_percent, disk_percent)
    log_to_file(cpu_usage, memory_usage, disk_usage)
            
    print(f"\n{Fore.GREEN}==========================================================={Style.RESET_ALL}")
    print(f"Actualizando cada 5 segundos. Presione {Fore.CYAN}Ctrl+C{Style.RESET_ALL} para salir.")
    time.sleep(5)

    
def start():
    try:
        while True:
            os.system('clear')

            banner()
            creditsLabel()
            monitor_resources()
    except:
        print(f"\n{Fore.GREEN}Monitor de recursos detenido.{Style.RESET_ALL}")


if __name__=="__main__":
    start()



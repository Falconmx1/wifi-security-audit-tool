import subprocess
import time
from colorama import Fore, Style

def capture_handshake(interface, bssid, channel):
    """Captura el handshake WPA"""
    print(f"{Fore.CYAN}[*] Configurando monitor en canal {channel}...{Style.RESET_ALL}")
    
    # Configurar canal
    subprocess.run(f"sudo iwconfig {interface} channel {channel}", shell=True)
    
    # Iniciar captura
    filename = f"handshake_{bssid.replace(':', '')}"
    cmd = f"sudo airodump-ng --bssid {bssid} --channel {channel} --write {filename} {interface}"
    
    print(f"{Fore.YELLOW}[!] Esperando handshake. Presiona Ctrl+C cuando se capture...{Style.RESET_ALL}")
    try:
        subprocess.run(cmd.split())
    except KeyboardInterrupt:
        print(f"{Fore.GREEN}[+] Captura guardada en {filename}-01.cap{Style.RESET_ALL}")
        return f"{filename}-01.cap"
    return None

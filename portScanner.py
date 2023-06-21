import socket
import termcolor

def scan(target, ports):
    print('\n' ' Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(targets, port)

def scan_port(ipaddress, port):
    try: 
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except: 
        pass

targets = input("[*] Enter Targetes To Scan(Split Them By ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else: 
    scan(targets, ports)
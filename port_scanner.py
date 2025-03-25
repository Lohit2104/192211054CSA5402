import socket 
 
def scan_ports(target, ports): 
    for port in ports: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(1) 
        result = sock.connect_ex((target, port)) 
        if result == 0: 
            print(f"Port {port} is open") 
        sock.close() 
 
target_ip = "192.168.1.1" 
ports_to_scan = [22, 80, 443, 8080] 
scan_ports(target_ip, ports_to_scan)

import nmap #install nmap and paste the path in the environment variables
 
def nmap_scan(target): 
    scanner = nmap.PortScanner() 
    scanner.scan(target, '1-1024', '-sS') 
    for port in scanner[target]['tcp']: 
        print(f"Port {port}: {scanner[target]['tcp'][port]['state']}") 
 
target_ip = "192.168.1.1" 
nmap_scan(target_ip)
import os
import scapy.all as scapy
import matplotlib.pyplot as plt
import numpy as np
import ipaddress
from collections import Counter

# Ensure script runs with admin privileges
if os.name == "nt" and os.system("net session >nul 2>&1") != 0:
    print("[ERROR] This script must be run as Administrator!")
    exit(1)

# Dictionary to store IP occurrences
ip_count = Counter()

def capture_packets(packet):
    """Capture packets and extract source and destination IPs."""
    if packet.haslayer(scapy.IP):
        ip_count[packet[scapy.IP].src] += 1
        ip_count[packet[scapy.IP].dst] += 1

# Capture 50 packets
print("[INFO] Capturing network packets... Press Ctrl+C to stop.")
try:
    scapy.sniff(prn=capture_packets, count=50, store=False)
except PermissionError:
    print("[ERROR] Scapy requires admin/root privileges to capture packets.")
    exit(1)

# Display captured IP addresses and their frequency
print("\n===== Captured IP Address Frequencies =====")
for ip, count in ip_count.items():
    print(f"{ip}: {count} packets")

# Visualization
ips = list(ip_count.keys())
counts = list(ip_count.values())

plt.figure(figsize=(10, 5))
plt.bar(ips, counts, color='blue')
plt.xticks(rotation=45, ha='right')
plt.xlabel("IP Addresses")
plt.ylabel("Number of Packets")
plt.title("IP Address Allocation Analysis")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Subnet Analysis (Public vs. Private IP Classification)
def classify_ip(ip):
    """Classifies IP as Public or Private."""
    try:
        ip_obj = ipaddress.ip_address(ip)
        return "Private IP" if ip_obj.is_private else "Public IP"
    except ValueError:
        return "Invalid IP"

print("\n===== IP Address Classification =====")
for ip in ip_count.keys():
    print(f"{ip}: {classify_ip(ip)}")

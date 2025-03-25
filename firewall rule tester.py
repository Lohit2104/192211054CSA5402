from scapy.all import * 
 
def test_firewall(destination_ip): 
    print(f"Sending test packet to {destination_ip}") 
    packet = IP(dst=destination_ip)/ICMP() 
    response = sr1(packet, timeout=2, verbose=0) 
     
    if response: 
        print("Packet Allowed: Firewall is not blocking ICMP requests.") 
    else: 
        print("Packet Blocked: Firewall is blocking ICMP requests.") 
 
if __name__ == "__main__": 
    target_ip = input("Enter the target IP: ") 
    test_firewall(target_ip)


#note to self: run vscode as admin to execute this program
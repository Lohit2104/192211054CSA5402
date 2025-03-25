import paramiko 
import socket 
import logging 
 
# Configure logging 
logging.basicConfig(filename="ssh_brute_force.log", level=logging.INFO, 
                    format="%(asctime)s - %(message)s") 
 
def detect_brute_force_attempts(server_ip, port, username, password_list): 
    """Detects failed SSH login attempts using Paramiko.""" 
    for password in password_list: 
        try: 
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(server_ip, port=port, username=username, 
password=password, timeout=5) 
            client.close() 
            print("Login successful with password:", password) 
            break 
        except paramiko.AuthenticationException: 
            logging.info(f"Failed login attempt for {username} with password: {password}") 
            print("Failed login attempt detected.") 
        except socket.error: 
            logging.error("Connection error occurred.") 
            break 
 
# Example usage 
server_ip = "192.168.1.1" 
port = 22 
username = "admin" 
password_list = ["password123", "admin123", "letmein", "123456"] 
 
detect_brute_force_attempts(server_ip, port, username, password_list) 
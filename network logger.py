import psutil
import time
import csv

def log_connections(log_file="network_connections.csv"):
    """Logs active network connections to a CSV file every 5 seconds."""
    with open(log_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "PID", "Local Address", "Remote Address", "Status", "Process Name"])

        while True:
            for conn in psutil.net_connections(kind='inet'):
                try:
                    laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                    raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                    process = psutil.Process(conn.pid).name() if conn.pid else "N/A"
                    writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), conn.pid, laddr, raddr, conn.status, process])
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            print("Logging network connections... Press Ctrl+C to stop.")
            time.sleep(5)  # Log every 5 seconds

if __name__ == "__main__":
    log_connections()
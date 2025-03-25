import hashlib
import time

# List of files to monitor
FILES_TO_MONITOR = ["C:\\Windows\\System32\\drivers\\etc\\hosts"]


def get_file_hash(filepath):
    """Returns the SHA256 hash of the file contents."""
    try:
        with open(filepath, 'rb') as file:
            file_contents = file.read()
            return hashlib.sha256(file_contents).hexdigest()
    except FileNotFoundError:
        return None

def monitor_files(interval=10):
    """Continuously monitors the files for unauthorized changes."""
    file_hashes = {file: get_file_hash(file) for file in FILES_TO_MONITOR}

    print("Monitoring started. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(interval)

            for file in FILES_TO_MONITOR:  # FIXED indentation
                new_hash = get_file_hash(file)
                if new_hash is None:
                    print(f"[ALERT] {file} has been deleted!")
                elif new_hash != file_hashes[file]:
                    print(f"[WARNING] Unauthorized change detected in {file}!")
                    file_hashes[file] = new_hash  # Update stored hash
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_files()
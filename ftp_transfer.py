from ftplib import FTP 
import os 
 
def upload_file(ftp_server, username, password, file_path): 
    ftp = FTP(ftp_server) 
    ftp.login(user=username, passwd=password) 
    with open(file_path, 'rb') as f: 
        ftp.storbinary(f'STOR {os.path.basename(file_path)}', f) 
    ftp.quit() 
    print(f"Encrypted file {file_path} uploaded successfully.") 
 
def download_file(ftp_server, username, password, remote_filename, local_path): 
    ftp = FTP(ftp_server) 
    ftp.login(user=username, passwd=password) 
    with open(local_path, 'wb') as f: 
        ftp.retrbinary(f'RETR {remote_filename}', f.write) 
    ftp.quit() 
    print(f"Encrypted file {remote_filename} downloaded successfully.") 
 
# Example Usage 
upload_file("ftp.example.com", "user", "password", "sample_encrypted.bin") #that ftp.example.com should be replaced with your own website or use local ftp from filezilla on windows
# download_file("ftp.example.com", "user", "password", "sample_encrypted.bin", "downloaded_encrypted.bin") 
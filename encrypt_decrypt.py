from Crypto.Cipher import AES 
import os 
 
def pad(data): 
    """Pads data to make it AES block size compliant.""" 
    return data + b" " * (16 - len(data) % 16) 
 
def encrypt_file(input_file, output_file, key): 
    """Encrypts a file using AES encryption.""" 
    cipher = AES.new(key, AES.MODE_ECB) 
    with open(input_file, 'rb') as f: 
        plaintext = f.read() 
    ciphertext = cipher.encrypt(pad(plaintext)) 
    with open(output_file, 'wb') as f: 
        f.write(ciphertext) 
    print(f"File {input_file} encrypted successfully as {output_file}.") 
 
def decrypt_file(input_file, output_file, key): 
    """Decrypts a file using AES encryption.""" 
    cipher = AES.new(key, AES.MODE_ECB) 
    with open(input_file, 'rb') as f: 
        ciphertext = f.read() 
    plaintext = cipher.decrypt(ciphertext).rstrip(b" ") 
    with open(output_file, 'wb') as f: 
        f.write(plaintext) 
    print(f"File {input_file} decrypted successfully as {output_file}.") 
 
# Example Usage 
key = b"thisisaverysecurekey!"[:16]  # Ensure 16 bytes long 
#Encrypt: encrypt_file("sample.txt", "sample_encrypted.bin", key) 
# Decrypt: decrypt_file("sample_encrypted.bin", "sample_decrypted.txt", key) 
from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes 
from Crypto.Util.Padding import pad, unpad 
from Crypto.Protocol.KDF import scrypt 
import base64 
 
# Function to generate a random key (AES-256 requires a 32-byte key) 
def generate_key(): 
    key = get_random_bytes(32)  # AES-256 key size 
    return key 
 
# Function to encrypt a message using AES-GCM 
def encrypt_message(key, message, aad=None): 
    # Generate a random 12-byte nonce (recommended size for GCM) 
    nonce = get_random_bytes(12) 
     
    # Create AES-GCM cipher object 
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce) 
     
    # Encrypt the message and return ciphertext, nonce, and tag 
    cipher.update(aad)  # Optional AAD (Additional Authenticated Data) 
    ciphertext, tag = cipher.encrypt_and_digest(message.encode()) 
     
    return ciphertext, nonce, tag 
 
# Function to decrypt a message using AES-GCM and verify its authenticity 
def decrypt_message(key, ciphertext, nonce, tag, aad=None): 
    # Create AES-GCM cipher object 
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce) 
     
    cipher.update(aad)  # Optional AAD (Additional Authenticated Data) 
     
    # Decrypt the message and verify the authenticity 
    try: 
        decrypted_message = cipher.decrypt_and_verify(ciphertext, tag) 
        return decrypted_message.decode() 
    except (ValueError, TypeError): 
        print("Decryption failed or message is tampered!") 
        return None 
 
# Main function to demonstrate AES-GCM encryption and decryption 
def main(): 
    # The message to be encrypted 
    message = "This is a confidential and authenticated message." 
     
    # Generate the AES key 
    key = generate_key() 
     
    # Encrypt the message 
    print("Encrypting message...") 
    aad = b"Additional Authenticated Data"  # Optional AAD 
    ciphertext, nonce, tag = encrypt_message(key, message, aad) 
     
     
    # Print the encrypted message details 
    print(f"Ciphertext (Base64): {base64.b64encode(ciphertext).decode()}") 
    print(f"Nonce (Base64): {base64.b64encode(nonce).decode()}") 
    print(f"Authentication Tag (Base64): {base64.b64encode(tag).decode()}") 
     
    # Decrypt the message 
    print("\nDecrypting message...") 
    decrypted_message = decrypt_message(key, ciphertext, nonce, tag, aad) 
     
    if decrypted_message: 
        print(f"Decrypted Message: {decrypted_message}") 
    else: 
        print("Failed to decrypt the message.") 
 
if __name__ == "__main__": 
    main()
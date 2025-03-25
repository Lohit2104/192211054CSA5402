from Crypto.PublicKey import RSA 
from Crypto.Signature import pkcs1_15 
from Crypto.Hash import SHA256 
from Crypto.Random import get_random_bytes 
import binascii 
 
# Function to generate RSA key pair 
def generate_keys(): 
    key = RSA.generate(2048)  # 2048-bit RSA key 
    private_key = key.export_key() 
    public_key = key.publickey().export_key() 
    return private_key, public_key 
 
# Function to create a digital signature 
def create_signature(message, private_key): 
    # Hash the message using SHA-256 
    h = SHA256.new(message.encode()) 
 
    # Load the private key 
    private_key_obj = RSA.import_key(private_key) 
 
    # Create the signature using the private key and hashed message 
    signature = pkcs1_15.new(private_key_obj).sign(h) 
    return signature 
 
# Function to verify the digital signature 
def verify_signature(message, signature, public_key): 
    # Hash the message 
    h = SHA256.new(message.encode()) 
 
    # Load the public key 
    public_key_obj = RSA.import_key(public_key) 
 
    try: 
        # Verify the signature using the public key 
        pkcs1_15.new(public_key_obj).verify(h, signature) 
        print("Signature is valid!") 
    except (ValueError, TypeError): 
        print("Signature verification failed!") 
 
# Main function 
if __name__ == "__main__": 
    # Step 1: Generate RSA keys 
    private_key, public_key = generate_keys() 
 
    # Step 2: Define a message 
    message = "This is a secret message!" 
 
    # Step 3: Create a digital signature for the message 
    print(f"Original Message: {message}") 
    signature = create_signature(message, private_key) 
 
    # Print the signature (in hexadecimal format) 
    print(f"Digital Signature: {binascii.hexlify(signature).decode()}") 
 
    # Step 4: Verify the digital signature 
    print("\nVerifying the signature with the public key...") 
    verify_signature(message, signature, public_key) 
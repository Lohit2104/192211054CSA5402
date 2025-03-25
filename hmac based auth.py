import hmac 
import hashlib 
import time 
 
# Secret key for HMAC (this should be kept secure) 
SECRET_KEY = b'supersecretkey' 
 
# Function to generate HMAC for a given message 
def generate_hmac(message, key): 
    return hmac.new(key, message.encode(), hashlib.sha256).hexdigest() 
 
# Function to verify the HMAC for a given message 
def verify_hmac(message, key, expected_hmac): 
    generated_hmac = generate_hmac(message, key) 
    return hmac.compare_digest(generated_hmac, expected_hmac) 
 
# Simulating a basic authentication process 
def authenticate_user(username, password): 
    # In a real-world scenario, the password would be hashed and stored securely 
    # Here, we simulate a stored password hash 
    stored_password_hash = generate_hmac("userpassword", SECRET_KEY) 
     
    # Verify the HMAC of the provided password against the stored hash 
    provided_password_hash = generate_hmac(password, SECRET_KEY) 
     
    if verify_hmac(provided_password_hash, SECRET_KEY, stored_password_hash): 
        print("Authentication Successful!") 
        return True 
    else: 
        print("Authentication Failed!") 
        return False 
 
# Simulating login attempt 
if __name__ == "__main__": 
    print("Welcome to the Secure Authentication System!") 
     
    username = input("Enter username: ") 
    password = input("Enter password: ") 
     
    # Authenticate the user with HMAC 
    authenticate_user(username, password) 
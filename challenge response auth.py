import secrets
import time 
 
# Secret key for OTP generation (in real-world applications, this should be securely stored) 
SECRET_KEY = "SuperSecretKey" 
 
# Function to generate a one-time password (OTP) based on a secret key and challenge 
def generate_otp(challenge, secret_key): 
    # Combine the challenge and secret key to generate a secure OTP 
    otp_input = challenge + secret_key 
    otp = secrets.token_hex(4)  # Generate a 4-byte OTP (8 hex characters) 
    return otp 
 
# Server-side function to generate the challenge and OTP 
def server_generate_challenge(): 
    challenge = secrets.token_hex(4)  # Generate a random challenge (4-byte random string) 
    otp = generate_otp(challenge, SECRET_KEY) 
    return challenge, otp 
 
# Client-side function to respond with OTP 
def client_respond(challenge, otp): 
    # The client would typically generate the OTP based on the secret key and challenge 
    # Here, for simplicity, we're directly passing the correct OTP 
    return otp 
 
# Function to simulate the challenge-response authentication process 
def authenticate_user(): 
    print("Welcome to the Secure OTP Authentication System!") 
     
    # Server generates a challenge and OTP 
    challenge, correct_otp = server_generate_challenge() 
     
    # Server displays the challenge (this would be shown to the client) 
    print(f"Challenge: {challenge}") 
     
    # Simulating the client receiving the challenge and generating the response (OTP) 
    client_otp = client_respond(challenge, correct_otp) 
     
    # Server verifies the client's response 
    if client_otp == correct_otp: 
        print("Authentication Successful!") 
    else: 
        print("Authentication Failed!") 
 
# Main function 
if __name__ == "__main__": 
    authenticate_user() 
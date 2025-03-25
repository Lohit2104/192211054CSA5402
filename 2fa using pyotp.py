import pyotp 
import time 
 
# Function to generate a secret key for 2FA 
def generate_secret(): 
    # Generate a random secret for the user (this is shared between client and server)
    totp = pyotp.TOTP(pyotp.random_base32()) 
    secret = totp.secret 
    print(f"Your secret key is: {secret}") 
    return secret 
 
# Function to generate OTP (this is typically done by the client) 
def generate_otp(secret): 
    totp = pyotp.TOTP(secret) 
    otp = totp.now()  # Generate a valid OTP based on the shared secret 
    print(f"Generated OTP: {otp}") 
    return otp 
 
# Function to verify OTP (this is typically done by the server) 
def verify_otp(secret, otp): 
    totp = pyotp.TOTP(secret) 
    if totp.verify(otp): 
        print("OTP Verified Successfully!") 
    else: 
        print("Invalid OTP! Verification Failed.") 
 
# Main function 
def main(): 
    print("Two-Factor Authentication (2FA) Demo") 
 
    # Step 1: Generate a secret (this would be shared between the server and the client) 
    secret = generate_secret() 
 
    # Step 2: Generate OTP (client generates OTP based on the shared secret) 
    otp = generate_otp(secret) 
 
    # Step 3: User enters the OTP (simulating client input here) 
    entered_otp = input("Enter the OTP: ") 
 
    # Step 4: Verify OTP (server verifies the OTP entered by the client) 
    verify_otp(secret, entered_otp) 
 
if __name__ == "__main__": 
    main()

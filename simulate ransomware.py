import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("encryption_key.key", "rb").read()

def encrypt_files(folder_path, key):
    cipher = Fernet(key)
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                file_data = file.read()
            encrypted_data = cipher.encrypt(file_data)

            # Correct indentation here
            with open(file_path, "wb") as file:
                file.write(encrypted_data)

    print("All files have been encrypted.")

def decrypt_files(folder_path, key):
    cipher = Fernet(key)
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = cipher.decrypt(encrypted_data)
            
            with open(file_path, "wb") as file:
                file.write(decrypted_data)

    print("All files have been decrypted.")

if __name__ == "__main__":
    folder = "C:/Users/akami/OneDrive/Desktop/comp int sec prgs/python/testfolder"  # Change to your target folder
    os.makedirs(folder, exist_ok=True)
    
    option = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()
    
    if option == 'E':
        key = generate_key()
        encrypt_files(folder, key)
    elif option == 'D':
        key = load_key()
        decrypt_files(folder, key)
    else:
        print("Invalid option. Use 'E' for encrypt or 'D' for decrypt.")


#run this as admin asw
#to see changes, check the testfolder you've created earlier and open one of the existing text files there to see the magic kekekeke
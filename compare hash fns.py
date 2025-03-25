import hashlib 
 
# Function to compute hash values for a given file using MD5, SHA-256, and SHA
512 
def compute_hash(file_path): 
    # Create empty dictionaries to store the hash values 
    hashes = {"MD5": "", "SHA-256": "", "SHA-512": ""} 
     
    # Open the file in binary mode 
    with open(file_path, 'rb') as file: 
        # Read the file in chunks to avoid memory overflow for large files 
        file_data = file.read() 
         
        # MD5 hash calculation 
        md5_hash = hashlib.md5() 
        md5_hash.update(file_data) 
        hashes["MD5"] = md5_hash.hexdigest() 
 
        # SHA-256 hash calculation 
        sha256_hash = hashlib.sha256() 
        sha256_hash.update(file_data) 
        hashes["SHA-256"] = sha256_hash.hexdigest() 
 
        # SHA-512 hash calculation 
        sha512_hash = hashlib.sha512() 
        sha512_hash.update(file_data) 
        hashes["SHA-512"] = sha512_hash.hexdigest() 
 
    return hashes 
 
# Function to compare hash values 
def compare_hashes(hashes): 
    print(f"MD5 Hash: {hashes['MD5']}") 
    print(f"SHA-256 Hash: {hashes['SHA-256']}") 
    print(f"SHA-512 Hash: {hashes['SHA-512']}") 
 
# Main function to test the hash functions 
if __name__ == "__main__": 
    file_path = input("Enter the path of the file to hash: ") 
    hashes = compute_hash(file_path) 
    compare_hashes(hashes) 
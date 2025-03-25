import hashlib
import bcrypt
import time

def hash_sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

def hash_bcrypt(data):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(data.encode('utf-8'), salt)

def compare_hashing_algorithms():
    data = "supersecretpassword"

    # SHA-256 hashing with better timing
    start_time = time.perf_counter()
    sha256_hash = hash_sha256(data)
    sha256_time = time.perf_counter() - start_time
    print(f"SHA-256 Hash: {sha256_hash}")
    print(f"SHA-256 Time: {sha256_time:.9f} seconds")

    # bcrypt hashing
    start_time = time.perf_counter()
    bcrypt_hash = hash_bcrypt(data)
    bcrypt_time = time.perf_counter() - start_time
    print(f"bcrypt Hash: {bcrypt_hash}")
    print(f"bcrypt Time: {bcrypt_time:.9f} seconds")

    # Comparing performance safely
    epsilon = 1e-9  # Prevent division by zero
    print("\nPerformance Comparison:")
    print(f"SHA-256 is faster than bcrypt by {bcrypt_time / (sha256_time + epsilon):.2f} times.")

if __name__ == "__main__":
    compare_hashing_algorithms()
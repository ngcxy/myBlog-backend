import os
from cryptography.fernet import Fernet

# Generate a new encryption key (You should keep this key secure and not share it)
encryption_key = Fernet.generate_key()

# Encrypt the AWS access key and secret access key using the encryption key
def encrypt_secret(secret):
    f = Fernet(encryption_key)
    encrypted_secret = f.encrypt(secret.encode())
    return encrypted_secret

# Decrypt the encrypted secret using the encryption key
def decrypt_secret(encrypted_secret):
    f = Fernet(encryption_key)
    decrypted_secret = f.decrypt(encrypted_secret).decode()
    return decrypted_secret

# Example usage:
aws_access_key = "YOUR_AWS_ACCESS_KEY"
aws_secret_key = "YOUR_AWS_SECRET_KEY"

# Encrypt the secrets before setting them as environment variables
encrypted_access_key = encrypt_secret(aws_access_key)
encrypted_secret_key = encrypt_secret(aws_secret_key)

# # Set the encrypted secrets as environment variables
# os.environ["ENCRYPTED_AWS_ACCESS_KEY"] = encrypted_access_key
# os.environ["ENCRYPTED_AWS_SECRET_KEY"] = encrypted_secret_key
#
# # Retrieve the encrypted secrets from environment variables
# encrypted_access_key = os.environ.get("ENCRYPTED_AWS_ACCESS_KEY")
# encrypted_secret_key = os.environ.get("ENCRYPTED_AWS_SECRET_KEY")
#
# # Decrypt the secrets before using them
# decrypted_access_key = decrypt_secret(encrypted_access_key)
# decrypted_secret_key = decrypt_secret(encrypted_secret_key)
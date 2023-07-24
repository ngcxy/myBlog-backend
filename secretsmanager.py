from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

access_key = b'gAAAAABkvdW7K3DIy0uiYxdS94_0Ebj0RH2gs4dz7w8gCLEEhLu1-9YPkgzXy6JWdW8tH3_gjLbT743DoLnvV3S3eNAb-4xUF2gWAx7AZ15ZRiB5ZbNB90c='
secret_key = b'gAAAAABkvdXvXgQvRUrlf8BYpnojTbBy1OteM5VUPl9nxtxLoZoUpNSN3lp7CypcrlBooa108tw2nqWfdH3cP1SV-NMWJmSf13pShHkR7WWyUeJaiLZ7NyjifnQBtRnYA-S4N7j0sHIm'


decrypted_access_key = fernet.decrypt(access_key).decode()
decrypted_secret_key = fernet.decrypt(secret_key).decode()

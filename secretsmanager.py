from cryptography.fernet import Fernet

encryption_key = Fernet.generate_key()

access_key = "b'gAAAAABkvdCGkNb0VEtUXvixXkWzr279fTBzRL1qbIwRc0vEOJmiWAB0QlvMjrdUnwUnem4XPqZzCJM_wUMXARDDn4f_CquHYN2g5AcTNUDixiMNy27usbY='"
secret_key = "b'gAAAAABkvdEtWyqYl-7Erst4FhzPYuWjTjW9HyoQOS6Y980wYldz0jyd1TIWzabMK5wkN0XbDGY8HA4XfxglwGiSaGK4hpRxG9Q8D_cM-4p4nZZDZFrIS11aztFWiTF3BGd2cbMlzItg'"


def decrypt_secret(encrypted_secret):
    f = Fernet(encryption_key)
    decrypted_secret = f.decrypt(encrypted_secret).decode()
    return decrypted_secret


decrypted_access_key = decrypt_secret(access_key)
decrypted_secret_key = decrypt_secret(secret_key)

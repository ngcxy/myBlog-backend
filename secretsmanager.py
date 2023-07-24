from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

access_key = "b'gAAAAABkvdCGkNb0VEtUXvixXkWzr279fTBzRL1qbIwRc0vEOJmiWAB0QlvMjrdUnwUnem4XPqZzCJM_wUMXARDDn4f_CquHYN2g5AcTNUDixiMNy27usbY='"
secret_key = "b'gAAAAABkvdEtWyqYl-7Erst4FhzPYuWjTjW9HyoQOS6Y980wYldz0jyd1TIWzabMK5wkN0XbDGY8HA4XfxglwGiSaGK4hpRxG9Q8D_cM-4p4nZZDZFrIS11aztFWiTF3BGd2cbMlzItg'"


decrypted_access_key = fernet.decrypt(access_key).decode()
decrypted_secret_key = fernet.decrypt(secret_key).decode()

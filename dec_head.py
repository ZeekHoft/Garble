import json
from decryption import Decryption
path = r"C:\Users\OJTVince\AppData\Local\garble\user_data.json"

class DecryptHead():
    def decrypt_head(self):
        with open(path, 'r') as f:
            words = json.load(f)
            # print(words)
            final_list_encryption = words['final_list_encryption']
            store_encrypted_int = words['store_encrypted_int']
            special_key_storage = words['special_key_storage']
            encrypted = words['encrypted']
            sol = Decryption(final_list_encryption, store_encrypted_int, special_key_storage, encrypted)
            print(sol.final_decryption()) #need output

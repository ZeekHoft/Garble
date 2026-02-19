import json
import os
from pathlib import Path
from decryption import Decryption
app_dir = Path(os.getenv('LOCALAPPDATA')) / "garble"
path = rf"{app_dir}\user_data.json"



class DecryptHead():
    
    def decrypt_head(self):
        with open(path, 'r') as f:
            words = json.load(f)
            # print(words)
            final_list_encryption = words['final_list_encryption']
            store_encrypted_int = words['store_encrypted_int']
            special_key_storage = words['special_key_storage']
            encrypted = words['encrypted']
            specialKey = words['special_key']
        
            print(specialKey)
            sol = Decryption(final_list_encryption, store_encrypted_int, special_key_storage, encrypted, specialKey)
            print(sol.final_decryption()) #need output

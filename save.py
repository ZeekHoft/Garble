import json
import os
from pathlib import Path
# This creates a path to: C:\Users\<YourUser>\AppData\Local\MyCoolApp
# It's 'deep', safe, and won't affect the PC's performance.

# class SaveData:

#     def __init__(self, passkey):
#         self.passkey = passkey

#     def secret_value(self):
#         value = self.passkey
#         return value





def save_user_data( enc_list,
                enc_int,
                enc_storage,
                enc_enc,
                special_key):
    app_dir = Path(os.getenv('LOCALAPPDATA')) / "garble"

    # Create the directory if it doesn't exist
    app_dir.mkdir(parents=True, exist_ok=True)

    file_path = app_dir / "user_data.json"
    string_path = str(app_dir)
    data_to_save = {
        "final_list_encryption": enc_list,
        "store_encrypted_int": enc_int,
        "special_key_storage": enc_storage,
        "encrypted": enc_enc,
        "secret_pat": string_path,
        "special_key": special_key
        
    }

    # Save the data
    with open(file_path, 'w') as f:
        json.dump(data_to_save, f)

    # print(f"File saved deeply asssssssssst: {string_path}")


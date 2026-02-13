import json
import os
from pathlib import Path
# This creates a path to: C:\Users\<YourUser>\AppData\Local\MyCoolApp
# It's 'deep', safe, and won't affect the PC's performance.

def save_user_data(enc_list, enc_int, enc_storage, enc_enc):
    app_dir = Path(os.getenv('LOCALAPPDATA')) / "garble"

    # Create the directory if it doesn't exist
    app_dir.mkdir(parents=True, exist_ok=True)

    file_path = app_dir / "user_data.json"

    data_to_save = {
        "final_list_encryption": enc_list,
        "store_encrypted_int": enc_int,
        "special_key_storage": enc_storage,
        "encrypted": enc_enc,
    }

    # Save the data
    with open(file_path, 'w') as f:
        json.dump(data_to_save, f)

    print(f"File saved deeply at: {file_path}")



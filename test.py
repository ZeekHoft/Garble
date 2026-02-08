import json
from decryption import Decryption, see_type
path = r"C:\Users\USER\AppData\Local\garble\user_data.json"

with open(path, 'r') as f:
    words = json.load(f)
    # print(words)
    final_list_encryption = (f"{(words['final_list_encryption'])}")
    store_encrypted_int = (f"{(words['store_encrypted_int'])}")
    special_key_storage = (f"{(words['special_key_storage'])}")
    encrypted = (f"{(words['encrypted'])}")
    convert_enc = encrypted.replace('[','').replace(']','').replace(',','')
    # print(final_list_encryption)
    # print(store_encrypted_int)
    # print(special_key_storage)
    # print(encrypted)
    print(convert_enc)
    see_type(encrypted)

    sol = Decryption(final_list_encryption, store_encrypted_int, special_key_storage, convert_enc)
    print(sol.final_decryption()) #need output

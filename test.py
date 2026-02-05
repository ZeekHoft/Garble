import json
from decryption import Decryption
path = r"C:\Users\OJTVince\AppData\Local\garble\user_data.json"


with open(path, 'r') as f:
    words = json.load(f)
    # print(words)
    val1 = (f"{(words['final_list_encryption'])}")
    val2 = (f"{(words['store_encrypted_int'])}")
    val3 = (f"{(words['remainder_process'])}")
    val4 = (f"{(words['special_key_storage'])}")
    val5 = (f"{(words['encrypted'])}")
    print(val1)
    print(val2)
    print(val3)
    print(val4)
    print(val5)

    # sol = Decryption(val1, val2, val3, val4, val5)
    # (sol.decryption_of_list())
    # (sol.list_number_decryption(sol.decryption_of_list()))
    # print(sol.final_decryption()) #need output
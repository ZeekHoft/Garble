# import sys
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
# # Increase the limit for integer <-> string conversion
# sys.set_int_max_str_digits(20000)

dictionary_encryption = {'0': 'K', '1': 'R', '2': 'B', '3': 'X', '4': 'Z', '5': 'A', '6': 'P', '7': 'M', '8': 'W', '9': 'Q'}
dictionary_decryption = {'K': '0', 'R': '1', 'B': '2', 'X': '3', 'Z': '4', 'A': '5', 'P': '6', 'M': '7', 'W': '8', 'Q': '9'}




# remainder_process = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 
# 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 
# 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]

# final_list_encryption = ['6', '9']
# store_encrypted_int = 69
# special_key_storage = 663
# encrypted = [747, 767, 768, 778, 695, 768, 778, 695, 760, 695, 778, 764, 762, 777, 764, 779, 695, 772, 764, 778, 778, 760, 766, 764, 695, 765, 777, 774, 772, 695, 781, 768, 773, 762, 764, 721, 695, 775, 774, 779, 760, 779, 774]


class Decryption:
    def __init__(self, final_list_encryption,
                 store_encrypted_int,
                 special_key_storage, encrypted,
                 specialKey):
        self.final_list_encryption = final_list_encryption
        self.store_encrypted_int = store_encrypted_int
        self.special_key_storage = special_key_storage
        self.encrypted = encrypted
        self.specialKey = specialKey
        self.__store_data_D()
    def __store_data_D(self):
        
        self.store_final_conversion  = []
        self.limit = 0
        self.decrypted_chars = []
        self.BLUE = Fore.BLUE
        self.RESET = Style.RESET_ALL

    def final_decryption(self):
        for val in self.encrypted:
            char_code = int(val) - int(self.special_key_storage)
            self.decrypted_chars.append(chr(char_code))
            
        path = input(f"{self.BLUE}file directory of the encrypted file\n(-U-): {self.RESET} ").upper()
        if not path:
            return ("Please input the file path of the encrypted file")
        else:
            secret = input(f"{self.BLUE}secret key\n(-U-): {self.RESET}")
            seperate = secret.split()
            if self.specialKey in seperate:
                with open(path, "w") as f:
                    f.write(''.join(self.decrypted_chars))
                return(f"{self.BLUE} DONE CHECK FILE (-U-) {self.RESET}")
         
            else:
                return ("INVALID KEY")

    def gui_decryption(self, target_path, secret):
        for val in self.encrypted:
            char_code = int(val) - int(self.special_key_storage)
            self.decrypted_chars.append(chr(char_code))

        if not target_path:
            return "Please input the file path of the encrypted file"
        else:
            seperate = secret.split()
            if self.specialKey in seperate:
                with open(target_path, "w") as f:
                    f.write(''.join(self.decrypted_chars))
                return "DONE CHECK FILE (-U-)"
            else:
                return "INVALID KEY"
    

# sol = Decryption(final_list_encryption,store_encrypted_int, special_key_storage, encrypted)
# # (sol.decryption_of_list())
# # (sol.list_number_decryption(sol.decryption_of_list()))
# print(sol.final_decryption()) #need output




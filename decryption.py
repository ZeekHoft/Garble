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
    # def decryption_of_list(self):
    #     decrypted_list  = []
    #     for i in self.final_list_encryption:
            
    #         if i not in dictionary_decryption.keys():
    #             decrypted_list.append(i)
               

    #         else:
    #             value = dictionary_decryption[i]
    #             decrypted_list.append(value)
    #     return([int(x) for x in decrypted_list])
        


    # def list_number_decryption(self, list_num):
    #     converted_number = int(''.join([str(i) for i in list_num]))
    #     store_converted = converted_number
    
    #     #stores all remainder
    #     while self.store_encrypted_int >= store_converted:
    #         self.remainder_process.append(self.store_encrypted_int % 2) #appends all remiander 0 and or 1 
    #         self.store_encrypted_int //= 2
    #     for r in reversed(self.remainder_process):
            
    #         store_converted = store_converted * 2 + r #adds remainders here

    #     #self.encryption has the right amount always so i need to gets one of its index 0, and get its len as reference
    #     convert_length = list(map(str, self.encrypted))
    #     for lengths in convert_length[0]:
    #         self.limit += len(lengths)


    #     conversion_store = str(store_converted)
    #     final_seperation = [(conversion_store)[i:i+self.limit] for i in range(0, len(conversion_store), self.limit)]
    #     self.store_final_conversion = [int(x) for x in final_seperation]
    #     # print("_____________________")
    #     # print(store_converted)
    #     # print(self.final_list_encryption)
    #     # print((self.store_encrypted_int))
    #     print(self.remainder_process)
    #     # print(self.encrypted)

        


            
    # def final_decryption(self):
    #     for i in range(len(self.store_final_conversion)):
    #         self.store_final_conversion[i] -= self.special_key_storage
            
    #     question = input("Decrypt (Y/N) if N all data will be lost: ").upper()
    #     if question == "Y":
    #         return (f"DECRYPTED: {''.join(map(chr, self.store_final_conversion))}")
    
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

           
            
           
        




        
    # def final_decryption(self):
    #     decrypted_chars = []
    #     for val in self.encrypted:
    #         # Subtract the special key to get the real ASCII value
    #         char_code = val - self.special_key_storage
    #         decrypted_chars.append(chr(char_code))
            
    #     question = input("Decrypt (Y/N): ").upper()
    #     if question == "Y":
    #         return f"DECRYPTED: {''.join(decrypted_chars)}"


# sol = Decryption(final_list_encryption,store_encrypted_int, special_key_storage, encrypted)
# # (sol.decryption_of_list())
# # (sol.list_number_decryption(sol.decryption_of_list()))
# print(sol.final_decryption()) #need output




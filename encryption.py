dictionary_encryption = {'0': 'K', '1': 'R', '2': 'B', '3': 'X', '4': 'Z', '5': 'A', '6': 'P', '7': 'M', '8': 'W', '9': 'Q'}
dictionary_decryption = {'K': '0', 'R': '1', 'B': '2', 'X': '3', 'Z': '4', 'A': '5', 'P': '6', 'M': '7', 'W': '8', 'Q': '9'}

# special_key = input("What will be the secret key (secret key, peacock, lions main): ")
# secret_word = input("What message would you like encrypted:  ")

from save import save_user_data
class Encrypt:
    # store all variables that can be accessible on every function
    def __init__(self, special_key, encrypt_word):
        self.special_key = special_key
        self.encrypt_word = encrypt_word
        self.__store_data_E()

    # self made method
    def __store_data_E(self):
        self.special_key_storage = 0
        self.encrypted = []
        self.encrypted_str = ""
        self.encrypted_int = 0
        self.store_encrypted_int = 0 #stores the biggest number
        self.final_list_encryption = []
        self.store_final_conversion = []
        self.encryption_output_limit = 2
        self.remainder_process = []
        self.limit = 0
        
    def generate_special_key(self):
        value = [ord(i) for i in self.special_key]
        for num in value:
            self.special_key_storage += num


    def encrypt_to_numbers(self):
        self.encrypted = [ord(i) + self.special_key_storage for i in self.encrypt_word]


    def encryption_conversion(self):
        self.encrypted_str = ''.join(map(str, self.encrypted))
        self.encrypted_int = int(self.encrypted_str)
        self.store_encrypted_int = self.encrypted_int
  
        while True:
            if len(str(self.encrypted_int)) == self.encryption_output_limit:
                break
            else:
                self.encrypted_int //= 2
    def final_encryption(self):
        itteration_conversion_str = str(self.encrypted_int)
        pos_1 = 0 
        pos_2 = 1
        
        for _ in range(len(itteration_conversion_str)//2):
            if pos_1 < (len(itteration_conversion_str)) and pos_2 < len(itteration_conversion_str):
                result = int(itteration_conversion_str[pos_1]) + int(itteration_conversion_str[pos_2])
                if (result % 2) ==0:
                    self.final_list_encryption.extend(dictionary_encryption[(itteration_conversion_str[pos_1])] + dictionary_encryption[(itteration_conversion_str[pos_2])]  )
                elif (result % 2) != 0:
                    self.final_list_encryption.extend([(itteration_conversion_str[pos_1])]+ [(itteration_conversion_str[pos_2])]  )
            pos_1 += 2
            pos_2 += 2
            
            save_user_data(self.final_list_encryption,
                                self.store_encrypted_int,
                                self.special_key_storage,
                                self.encrypted,
                                self.special_key )
        return(' '.join(self.final_list_encryption))
            

    


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
        # print(sum(value))
        for num in value:
            self.special_key_storage += num
        # return self.special_key_storage


    def encrypt_to_numbers(self):
        # print([ord(i) for i in self.encrypt_word]) # #original ascii form
        self.encrypted = [ord(i) + self.special_key_storage for i in self.encrypt_word]
        # return (self.encrypted) #returns the list thats encrypted

    def encryption_conversion(self):
        self.encrypted_str = ''.join(map(str, self.encrypted))
        self.encrypted_int = int(self.encrypted_str)
        self.store_encrypted_int = self.encrypted_int
  
        while True:
            if len(str(self.encrypted_int)) == self.encryption_output_limit:
                break
            else:
                self.encrypted_int //= 2
        # return self.encrypted_int #returns the divided till 6 values
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
            
            # print("_____________________")
            # print(self.special_key_storage)
            # print(self.final_list_encryption)
            # print(self.store_encrypted_int)
            # print(self.special_key_storage)
            # print(self.encrypted)
            save_user_data(self.final_list_encryption,
                                self.store_encrypted_int,
                                self.special_key_storage,
                                self.encrypted )
        return(' '.join(self.final_list_encryption))
            

    

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
    #     while self.store_encrypted_int > store_converted:
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
    #     # need these 3 values to be passed so that decryption will work


    


            
    # def final_decryption(self):
    #     for i in range(len(self.store_final_conversion)):
    #         self.store_final_conversion[i] -= self.special_key_storage
            
    #     question = input("Decrypt (Y/N) if N all data will be lost: ").upper()
    #     if question == "Y":
    #         print(self.special_key_storage)
    #         return (f"DECRYPTED: {' '.join(map(chr, self.store_final_conversion))}")
        
  
# sol = Encrypt(special_key, secret_word)
# sol.generate_special_key()
# (sol.encrypt_to_numbers()) #turn the ascii numbers and add more complexity to them
# (sol.encryption_conversion()) #convert the list to string then to int then divide
# print(sol.final_encryption()) #need output




# (sol.decryption_of_list())
# (sol.list_number_decryption(sol.decryption_of_list()))
# print(sol.final_decryption()) #need output
# print(sol.decrypt(sol.generate_special_key()))
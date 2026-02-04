dictionary_encryption = {'0': 'K', '1': 'R', '2': 'B', '3': 'X', '4': 'Z', '5': 'A', '6': 'P', '7': 'M', '8': 'W', '9': 'Q'}
dictionary_decryption = {'K': '0', 'R': '1', 'B': '2', 'X': '3', 'Z': '4', 'A': '5', 'P': '6', 'M': '7', 'W': '8', 'Q': '9'}



final_list_encryption = ['W', 'P']
remainder_process = [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
store_encrypted_int = 86


class Decryption:
    def __init__(self, final_list_encryption,store_encrypted_int, remainder_process):
        self.final_list_encryption = final_list_encryption
        self.remainder_process = remainder_process
        self.store_encrypted_int = store_encrypted_int
        
        self.__store_data_D()
    def __store_data_D(self):
        self.special_key_storage = 663
        self.encrypted = [775, 764, 774, 775, 771, 764]
        self.store_final_conversion  = []
        self.limit = 0

    def decryption_of_list(self):
        decrypted_list  = []
        for i in self.final_list_encryption:
            
            if i not in dictionary_decryption.keys():
                decrypted_list.append(i)
               

            else:
                value = dictionary_decryption[i]
                decrypted_list.append(value)
        return([int(x) for x in decrypted_list])
        


    def list_number_decryption(self, list_num):
        converted_number = int(''.join([str(i) for i in list_num]))
        store_converted = converted_number
    
        #stores all remainder
        while self.store_encrypted_int > store_converted:
            self.remainder_process.append(self.store_encrypted_int % 2) #appends all remiander 0 and or 1 
            self.store_encrypted_int //= 2
        for r in reversed(self.remainder_process):
            
            store_converted = store_converted * 2 + r #adds remainders here

        #self.encryption has the right amount always so i need to gets one of its index 0, and get its len as reference
        convert_length = list(map(str, self.encrypted))
        for lengths in convert_length[0]:
            self.limit += len(lengths)


        conversion_store = str(store_converted)
        final_seperation = [(conversion_store)[i:i+self.limit] for i in range(0, len(conversion_store), self.limit)]
        self.store_final_conversion = [int(x) for x in final_seperation]
        # print("_____________________")
        # print(store_converted)
        # print(self.final_list_encryption)
        # print((self.store_encrypted_int))
        # print(self.remainder_process)
        # print(self.encrypted)

        


            
    def final_decryption(self):
        for i in range(len(self.store_final_conversion)):
            self.store_final_conversion[i] -= self.special_key_storage
            
        question = input("Decrypt (Y/N) if N all data will be lost: ").upper()
        if question == "Y":
            return (f"DECRYPTED: {' '.join(map(chr, self.store_final_conversion))}")


sol = Decryption(final_list_encryption,store_encrypted_int, remainder_process)
(sol.decryption_of_list())
(sol.list_number_decryption(sol.decryption_of_list()))
print(sol.final_decryption()) #need output



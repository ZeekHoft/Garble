


from encryption import Encrypt
from dec_head import DecryptHead
# from save import SaveData
import colorama
from colorama import Fore, Style
# This line is the magic trick that makes colors work on Windows
colorama.init(autoreset=True)


import cmd
# path = r"C:\Users\USER\Documents\Codes\python projs\crypt\New folder\test.txt"
# C:\Users\Documents\njs front\test.txt




class  GarbleCLI(cmd.Cmd):


    def __init__(self):
        self.RED = Fore.RED
        self.GREEN = Fore.GREEN
        self.RESET = Style.RESET_ALL

        self.file_path = "C:\\Users\\Username\\Documents\\example.txt"
        self.in_garble = f"""\nWhen using garble, make sure to inlcude the file you want to encryp at the very end of the file path. \nE.G: '{ self.file_path} \n
        """

        super().__init__()
        self.prompt = f"{self.GREEN}(0v0): {self.RESET}"
        self.intro = '''
 ██████╗  █████╗ ██████╗ ██████╗ ██╗     ███████╗                                 
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝                                 
██║  ███╗███████║██████╔╝██████╔╝██║     █████╗                                   
██║   ██║██╔══██║██╔══██╗██╔══██╗██║     ██╔══╝                                   
╚██████╔╝██║  ██║██║  ██║██████╔╝███████╗███████╗                                 
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝                                 
                                                                                  
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                                                                     
A CLI TOOL MADE FOR ENCRYPTING FILE CREATED BY ZEEKHOFT AS A SIMPLE PROJECT NOW AT YOU SYSTEM :-]

'''




    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")
        
    def do_quit(self, line):
        """Exit the CLI."""
        return True
    def do_garble(self, line):
        """File encryption"""
        

        print(f" {self.in_garble}")
        
        try:
            path = input(rf"{self.RED}(0_0): {self.RESET}")
            if not path:
                print(f"{self.RED}Error: Path cannot be empty.{self.RESET}")
                return self.do_garble(line)
            
            special_key = input(f"{self.RED}Enter a special key words/numbers/sentence/special characters\n(0_0): {self.RESET}")  
            if not special_key:
                print(f"{self.RED}Error: Special Key cannot be empty.{self.RESET}")
                return self.do_garble(line)
            
            with open(path, 'r') as f:
                words = (f.readline())
            secret_word = words
            sol = Encrypt(special_key, secret_word)
            sol.generate_special_key()
            (sol.encrypt_to_numbers()) #turn the ascii numbers and add more complexity to them
            (sol.encryption_conversion()) #convert the list to string then to int then divide
         
            value = (sol.final_encryption()) #need output
            with open(path, "w") as f:
                f.write(value)
            print(f"{self.RED}ENCRYPTED FILE{self.RESET}")
            return True

            
            # (sol.decryption_of_list())
            # (sol.list_number_decryption(sol.decryption_of_list()))
            # print(sol.final_decryption()) #need output
        except FileNotFoundError:
            print(f"Invalid input EXITING. Rerun 'garble' and try a similar file path as this: {self.file_path}")
            return True

    def do_ungarble(self, line):
        """File Decryption"""
        try:
            sol = DecryptHead()
            sol.decrypt_head()
            return True

        except Exception as e:
            print(f"ERROR: {e}")
            return True


    
        
if __name__ == '__main__':
     GarbleCLI().cmdloop()

import cmd
# path = r"C:\Users\USER\Documents\Codes\python projs\crypt\New folder\test.txt"


class MyCLI(cmd.Cmd):
    prompt = '(0v0):'
    intro = '''
    
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
        file_path = "C:\\Users\\Username\\Documents\\example.txt"

        print("When using bargle, make sure to inlcude the file you want to encryp at the very end of the file path. \n" \
        f"Example would be: '{file_path}'")
        path = input(r"(0_0):")

        from encryption import Encrypt
        with open(path, 'r') as f:
            words = (f.readline())
        special_key = "potato"
        secret_word = words
        sol = Encrypt(special_key, secret_word)
        sol.generate_special_key()
        (sol.encrypt_to_numbers()) #turn the ascii numbers and add more complexity to them
        (sol.encryption_conversion()) #convert the list to string then to int then divide
        print(sol.final_encryption()) #need output

        (sol.decryption_of_list())
        (sol.list_number_decryption(sol.decryption_of_list()))
        print(sol.final_decryption()) #need output




if __name__ == '__main__':
    MyCLI().cmdloop()


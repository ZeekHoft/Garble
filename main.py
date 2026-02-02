
import cmd


# from encryption import Encrypt
# with open("test.txt") as f:
#     words = (f.readline())
# special_key = "potato"
# secret_word = words


# sol = Encrypt(special_key, secret_word)
# sol.generate_special_key()
# (sol.encrypt_to_numbers()) #turn the ascii numbers and add more complexity to them
# (sol.encryption_conversion()) #convert the list to string then to int then divide
# print(sol.final_encryption()) #need output
# print(sol.breakdown())

# (sol.decryption_of_list())
# (sol.list_number_decryption(sol.decryption_of_list()))
# print(sol.final_decryption()) #need output

class MyCLI(cmd.Cmd):
    prompt = '[;-)]:'
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_quit(self, line):
        """Exit the CLI."""
        return True
    


if __name__ == '__main__':
    MyCLI().cmdloop()
# Garble Encryption
```
 ██████╗  █████╗ ██████╗ ██████╗ ██╗     ███████╗                                   
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝                                   
██║  ███╗███████║██████╔╝██████╔╝██║     █████╗                                     
██║   ██║██╔══██║██╔══██╗██╔══██╗██║     ██╔══╝                                     
╚██████╔╝██║  ██║██║  ██║██████╔╝███████╗███████╗                                   
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝                                   
                                                                                    
███████╗███╗   ██║ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██║
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                                                                                                                                       
A CLI TOOL MADE FOR ENCRYPTING FILE CREATED BY ZEEKHOFT AS A SIMPLE PROJECT NOW AT YOU SYSTEM (0v0):
```
### Installation
Clone the repository to your local machine:

```
git clone [https://github.com/ZeekHoft/Garble.git](https://github.com/ZeekHoft/Garble.git)
```
```
cd Garble
```
```
pip install requirements.txt
or
python -m pip install requirements.txt
```
```
python main.py
```

## How to use

- **Prerequisites:** Python 3.8+ installed. Make a backup of any files you will encrypt.
- **Start the app:**

```
python main.py
```

- **Encrypt a file:**
	1. In the interactive prompt type `garble` and press Enter.
	2. When asked, enter the full path to the file you want to encrypt (include the filename at the end of the path).
	3. The tool reads the file, encrypts its contents, and overwrites the file with the encrypted output. Example input prompt:

```
(0_0): C:\path\to\your\file.txt
```

- **Decrypt a file:**
	1. In the interactive prompt type `ungarble` and press Enter.
	2. Follow any prompts shown by the tool to complete decryption.

- **Notes & safety:**
	- Always keep backups; encryption will overwrite the original file.
	- This is a learning/demo project; do not use for sensitive data without auditing and improving the cryptography.

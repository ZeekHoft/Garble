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

THE DECRYPTION ONLY WORKS ON THE SYSTEM IT'S BEING ENCRYPTED ON BECAUSE WITHIN THE CODE SOME OF THE DATA BEING STORED IS WITHIN YOUR SYSTEM, BURRIED DEEP DOWN YOUR SYSTEM

```
### Sample View
<img width="1389" height="799" alt="Screenshot 2026-03-10 062157" src="https://github.com/user-attachments/assets/aee2b740-0f75-44f2-90b6-8ef588850b0d" />


### Installation
Clone the repository to your local machine:

```
git clone [https://github.com/ZeekHoft/Garble.git](https://github.com/ZeekHoft/Garble.git)
```
```
cd Garble
```
```
pip install textual
```
```
python test.py
```

## How to use

- **Prerequisites:** Python 3.8+ installed. Make a backup of any files you will encrypt.
- **Start the app:**

```
python test.py
```

- **Encrypt a file (Garble):**
	1. In the Textual interface, input the absolute path to your file (e.g., `C:\path\to\your\file.txt`).
	2. Input your desired special key.
	3. Click the `Encrypt (Garble)` button or navigate to it and press Enter. The tool reads the file, encrypts its contents, and overwrites the file with the encrypted output. 
	4. A success message will appear in the system log below.

- **Decrypt a file (Ungarble):**
	1. In the Textual interface, input the absolute path to your file (e.g., `C:\path\to\your\file.txt`).
	2. Input the special key you used previously.
	3. Click the `Decrypt (Ungarble)` button. 
    4. The decrypted result will be printed out in the system log.

- **Notes & safety:**
	- Always keep backups; encryption will overwrite the original file.
	- This is a learning/demo project; do not use for sensitive data without auditing and improving the cryptography.

import os
import json
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Header, Footer, Input, Button, Log, Static
from textual.binding import Binding

from encryption import Encrypt
from decryption import Decryption

css = """
Screen {
    background: #282a36;
}

Header {
    background: #44475a;
    color: #f8f8f2;
    text-style: bold;
}

Footer {
    background: #44475a;
    color: #f8f8f2;
}

Input {
    border: solid #6272a4;
    background: #282a36;
    color: #f8f8f2;
    margin: 1 2;
}

Input:focus {
    border: double #bd93f9;
}

#controls {
    height: auto;
    align: center middle;
    margin: 1 2;
}

Button {
    background: #6272a4;
    color: #f8f8f2;
    border: none;
    margin: 0 2;
}

Button:hover {
    background: #bd93f9;
    color: #282a36;
}

Button.-active {
    background: #ff79c6;
}

Log {
    border: solid #6272a4;
    background: #21222c;
    color: #f8f8f2;
    height: 1fr;
    margin: 0 2;
}

.title {
    color: #8be9fd;
    text-style: bold;
    padding: 1;
    content-align: center middle;
    width: 100%;
}
"""

class GarbleApp(App):
    """A Textual app for Garble encryption/decryption with Linux distro style."""

    CSS = css
    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("Garble System Utility", classes="title")
        with Container():
            yield Input(placeholder="Target File Path (e.g. /home/user/file.txt)...", id="file_path")
            yield Input(placeholder="Special Key...", id="special_key", password=True)
            with Horizontal(id="controls"):
                yield Button("Encrypt (Garble)", id="btn_garble")
                yield Button("Decrypt (Ungarble)", id="btn_ungarble")
            yield Log(id="sys_log")
        yield Footer()

    def on_mount(self) -> None:
        self.theme = "textual-dark"
        self.log_to_ui("System initialized: Garble utility ready.")

    def log_to_ui(self, message: str) -> None:
        log_widget = self.query_one("#sys_log", Log)
        log_widget.write(f"[System] -> {message}\n")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        file_path = self.query_one("#file_path", Input).value.strip()
        special_key = self.query_one("#special_key", Input).value.strip()

        if event.button.id == "btn_garble":
            if not file_path or not special_key:
                self.log_to_ui("ERROR: File Path and Special Key cannot be empty for garbling.")
                return

            self.log_to_ui(f"Initiating garble on {file_path}...")
            try:
                with open(file_path, 'r') as f:
                    words = f.readline()
                
                if not words:
                    self.log_to_ui("WARNING: File is empty or could not be read.")
                    return

                sol = Encrypt(special_key, words)
                sol.generate_special_key()
                sol.encrypt_to_numbers()
                sol.encryption_conversion()
                value = sol.final_encryption()
                
                with open(file_path, "w") as f:
                    f.write(value)

                self.log_to_ui("SUCCESS: File GARBLED completely.")

            except FileNotFoundError:
                self.log_to_ui(f"ERROR: Could not find file at '{file_path}'.")
            except Exception as e:
                self.log_to_ui(f"CRITICAL ERROR: {e}")

        elif event.button.id == "btn_ungarble":
            if not file_path or not special_key:
                self.log_to_ui("ERROR: File Path and Special Key cannot be empty for ungarbling.")
                return

            self.log_to_ui("Initiating ungarble...")
            app_dir = Path(os.getenv('LOCALAPPDATA', '')) / "garble"
            data_path = app_dir / "user_data.json"
            
            if not os.path.exists(data_path):
                self.log_to_ui(f"ERROR: User data not found at {data_path}.")
                return

            try:
                with open(data_path, 'r') as f:
                    words = json.load(f)
                
                final_list_encryption = words.get('final_list_encryption')
                store_encrypted_int = words.get('store_encrypted_int')
                special_key_storage = words.get('special_key_storage')
                encrypted = words.get('encrypted')
                specialKey = words.get('special_key')

                self.log_to_ui("Encryption keys loaded.")
                
                sol = Decryption(final_list_encryption, store_encrypted_int, special_key_storage, encrypted, specialKey)
                decrypted_val = sol.gui_decryption(file_path, special_key)
                
                self.log_to_ui(f"DECRYPTED VALUE: {decrypted_val}")

            except Exception as e:
                self.log_to_ui(f"CRITICAL ERROR: {e}")

if __name__ == "__main__":
    app = GarbleApp()
    app.run()
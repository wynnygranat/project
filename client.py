import threading
from socket import *
from customtkinter import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.configure(fg_color='khaki')
        self.title("крутий чат")

        self.chat_field = CTkTextbox(self, font=('sans-serif', 20), state='disabled', text_color="black", fg_color='white')
        self.chat_field.pack(padx=10, pady=10, fill='both', expand=True)

        frame = CTkFrame(self)
        frame.pack(padx=10, pady=5, fill='x')

        self.message_entry = CTkEntry(frame, placeholder_text='Введіть повідомлення -->:')
        self.message_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))

        self.send_button = CTkButton(frame, text='Надіслати', command=self.send_message, fg_color="orange",hover_color="yellow", text_color='black')
        self.send_button.pack(side='right')

        self.username = 'Artem'
        self.sock = socket(AF_INET, SOCK_STREAM)
        try:
            self.sock.connect(('localhost', 8080))
            hello = f"TEXT@{self.username}@[SYSTEM] {self.username} приєднався до чату!\n"
            self.sock.send(hello.encode('utf-8'))
            threading.Thread(target=self.recv_message, daemon=True).start()
        except Exception as e:
            self.add_message(f"[Система] Не вдалося підключитися: {e}")

    def add_message(self, text):
        self.chat_field.configure(state='normal')
        self.chat_field.insert(END, text + '\n')
        self.chat_field.configure(state='disabled')
        self.chat_field.see(END)

    def send_message(self):
        message = self.message_entry.get().strip()
        if message:
            self.add_message(f"Я: {message}")
            data = f"TEXT@{self.username}@{message}\n"
            try:
                self.sock.sendall(data.encode())
            except:
                self.add_message("[Система] Не вдалося надіслати повідомлення.")
            self.message_entry.delete(0, END)

    def recv_message(self):
        buffer = ""
        while True:
            try:
                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                buffer += chunk.decode()
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    self.handle_line(line.strip())
            except:
                break
        self.sock.close()

    def handle_line(self, line):
        parts = line.split("@", 2)
        if len(parts) >= 3 and parts[0] == "TEXT":
            author = parts[1]
            message = parts[2]
            if author != self.username:
                self.add_message(f"{author}: {message}")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

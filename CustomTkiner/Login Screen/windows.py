import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Login Window')
app.geometry("400x300")
app.resizable(False, False)

def login_callback():
    username = entry_username.get()
    password = entry_password.get()
    if username == "azurion" and password == "bike4000%":
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid credentials")

frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill='both', expand=True)

label = ctk.CTkLabel(frame, text="Login")
label.pack(pady=10)

entry_username = ctk.CTkEntry(frame, placeholder_text="Username")
entry_username.pack(pady=5)

entry_password = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
entry_password.pack(pady=5)

button_login = ctk.CTkButton(frame, text="Login", command=login_callback)
button_login.pack(pady=10)

app.mainloop()

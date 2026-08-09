import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_file():
    file_path = filedialog.askopenfilename(title="Select file to encrypt")

    if not file_path:
        return

    try:
        key = AESGCM.generate_key(bit_length=256)
        aesgcm = AESGCM(key)

        with open(file_path, "rb") as file:
            data = file.read()

        nonce = os.urandom(12)
        encrypted_data = aesgcm.encrypt(nonce, data, None)

        output_file = file_path + ".enc"

        with open(output_file, "wb") as file:
            file.write(nonce + encrypted_data)

        key_text = base64.urlsafe_b64encode(key).decode()

        messagebox.showinfo(
            "Encryption Successful",
            f"Encrypted file:\n{output_file}\n\n"
            f"IMPORTANT - Save this key:\n{key_text}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def decrypt_file():
    file_path = filedialog.askopenfilename(
        title="Select encrypted file",
        filetypes=[("Encrypted files", ".enc"), ("All files", ".*")]
    )

    if not file_path:
        return

    key_window = tk.Toplevel(root)
    key_window.title("Enter Encryption Key")
    key_window.geometry("450x150")

    tk.Label(
        key_window,
        text="Enter the AES-256 key:"
    ).pack(pady=10)

    key_entry = tk.Entry(key_window, width=55)
    key_entry.pack()

    def perform_decryption():
        try:
            key_text = key_entry.get().strip()
            key = base64.urlsafe_b64decode(key_text)
            aesgcm = AESGCM(key)

            with open(file_path, "rb") as file:
                encrypted_data = file.read()

            nonce = encrypted_data[:12]
            ciphertext = encrypted_data[12:]

            decrypted_data = aesgcm.decrypt(
                nonce,
                ciphertext,
                None
            )

            output_file = file_path[:-4] + ".decrypted"

            with open(output_file, "wb") as file:
                file.write(decrypted_data)

            messagebox.showinfo(
                "Decryption Successful",
                f"Decrypted file:\n{output_file}"
            )

            key_window.destroy()

        except Exception as e:
          messagebox.showerror(
              "Decryption Failed",
              f"{type(e).__name__}: {e}"
    )

    tk.Button(
        key_window,
        text="Decrypt",
        command=perform_decryption
    ).pack(pady=15)


root = tk.Tk()
root.title("Advanced Encryption Tool - AES-256")
root.geometry("500x300")

title = tk.Label(
    root,
    text="AES-256 File Encryption Tool",
    font=("Arial", 18, "bold")
)
title.pack(pady=30)

encrypt_button = tk.Button(
    root,
    text="Encrypt File",
    width=25,
    height=2,
    command=encrypt_file
)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(
    root,
    text="Decrypt File",
    width=25,
    height=2,
    command=decrypt_file
)
decrypt_button.pack(pady=10)

root.mainloop()
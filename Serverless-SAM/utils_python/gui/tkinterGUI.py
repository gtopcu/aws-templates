
# https://docs.python.org/3/library/tkinter.html

import tkinter as tk
from tkinter import scrolledtext

def send_message():
    message = entry.get()
    if message:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + "\n")
        chat_box.see(tk.END)
        chat_box.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

def receive_message():
    message = "Sample reply" # Replace this with your actual logic to generate a reply
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Bot: " + message + "\n")
    chat_box.see(tk.END)
    chat_box.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Chat GUI")

# Chat history display
chat_box = scrolledtext.ScrolledText(root, width=50, height=20, state=tk.DISABLED)
chat_box.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Entry for user input
entry = tk.Entry(root, width=40)
entry.grid(row=1, column=0, padx=5, pady=5)

# Button to send message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=5, pady=5)

# Button to receive message (simulate bot response)
receive_button = tk.Button(root, text="Receive", command=receive_message)
receive_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

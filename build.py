import tkinter as tk
from tkinter import messagebox
import os
import git
import subprocess

def on_push():
    root_dir = root_dir_entry.get()
    git_url = git_url_entry.get()
    
    try:
        repo = git.Repo.init(root_dir)
        repo.git.add(A=True)
        repo.git.commit('-m', 'Auto commit')
        repo.git.branch('-M', 'main')  # Set the branch name to 'main'
        repo.create_remote('custom_remote', git_url)
        repo.git.push('custom_remote', 'main')  # Push to the 'main' branch
        messagebox.showinfo("Success", "Pushed to the 'main' branch on your custom remote repository.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("Git Pusher")

# Set the background color
root.configure(bg="#F0F0F0")

img = tk.PhotoImage(file="git_img.png")  # Replace with your image file path
img_label = tk.Label(root, image=img, bg="#F0F0F0")
img_label.pack()
# Create and configure GUI components (labels, entry fields, buttons, etc.)
root_dir_label = tk.Label(root, text="Root Directory:", bg="#F0F0F0")
root_dir_label.pack()

root_dir_entry = tk.Entry(root)
root_dir_entry.pack()

git_url_label = tk.Label(root, text="Git Repository URL:", bg="#F0F0F0")
git_url_label.pack()

git_url_entry = tk.Entry(root)
git_url_entry.pack()

push_button = tk.Button(root, text="Push to Git", command=on_push, bg="#007acc", fg="white")
push_button.pack()

# Add an image

# Create a label with highlighted text
developer_name_label = tk.Label(root, text="Developer: RC Balaji", bg="#F0F0F0", fg="#FF5733")
developer_name_label.pack()

root.mainloop()

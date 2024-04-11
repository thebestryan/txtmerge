import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import glob

def merge_files(folder_path):
    text_files = glob.glob(os.path.join(folder_path, '*.*'))
    if not text_files:
        messagebox.showinfo("Info", "No files found in the folder.")
        return

    extension = os.path.splitext(text_files[0])[1]
    merged_file_path = os.path.join(folder_path, f'merged{extension}')

    with open(merged_file_path, 'w') as outfile:
        for filename in text_files:
            with open(filename, 'r') as infile:
                outfile.write(infile.read() + "\n")

    messagebox.showinfo("Success", f"All files have been merged into {merged_file_path}")

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        merge_files(folder_path)

def main():
    root = tk.Tk()
    root.title("File Merger")

    tk.Label(root, text="Select a folder to merge files:", padx=20, pady=20).pack()
    tk.Button(root, text="Browse Folder", command=browse_folder, padx=20, pady=10).pack()
    tk.Button(root, text="Exit", command=root.destroy, padx=20, pady=10).pack()

    root.mainloop()

if __name__ == "__main__":
    main()

import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to remove content inside square brackets in lines starting with "Dealt to"
def remove_bracket_content(line):
    # Only apply modification if the line starts with "Dealt to"
    if line.startswith("Dealt to"):
        # Regex to remove content inside square brackets but keep the brackets
        return re.sub(r'\[.*?\]', '[]', line)
    return line  # Return the line unchanged if it doesn't start with "Dealt to"

# Function to process files and remove content inside square brackets
def process_files(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", f"Folder not found: {folder_path}")
        return

    # Traverse all files in the folder and subdirectories
    for root, _, files in os.walk(folder_path):
        for filename in files:
            # Only process .txt files
            if filename.endswith(".txt"):
                file_path = os.path.join(root, filename)

                # Read the file content
                with open(file_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()

                # Process each line and remove content inside square brackets where appropriate
                new_lines = []
                for line in lines:
                    # Apply the bracket removal function to each line
                    new_line = remove_bracket_content(line)
                    new_lines.append(new_line)

                # Save the processed file (overwrite the original)
                with open(file_path, "w", encoding="utf-8") as file:
                    file.writelines(new_lines)

    # Show a success message
    messagebox.showinfo("Success", "Processing complete! Hole cards has been removed.")

# Function to open folder dialog
def open_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, tk.END)  # Clear existing text
        folder_entry.insert(0, folder_selected)  # Insert selected path

# Function to trigger file processing
def start_processing():
    folder_path = folder_entry.get()  # Get folder path from entry widget
    process_files(folder_path)

# Set up the main window
root = tk.Tk()
root.title("Poker Hand Log Processor")

# Window dimensions
root.geometry("400x200")

# Folder selection UI elements
folder_label = tk.Label(root, text="Select Folder with Poker Hand Logs:")
folder_label.pack(pady=10)

folder_entry = tk.Entry(root, width=50)
folder_entry.pack(pady=5)

folder_button = tk.Button(root, text="Browse", command=open_folder)
folder_button.pack(pady=5)

# Process button
process_button = tk.Button(root, text="Process Files", command=start_processing)
process_button.pack(pady=20)

# Start the GUI loop
root.mainloop()

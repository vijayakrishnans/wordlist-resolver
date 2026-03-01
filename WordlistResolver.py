import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
#https://docs.python.org/3/library/os.html
#https://docs.python.org/3/library/tkinter.html
# Function to read content from a text file
def gettingFile(filePath):
    try:
        with open(filePath, 'r') as fP:
            content = fP.read()
        return content
    except FileNotFoundError:
        messagebox.showerror('Error', f'File not found: {filePath}')
        return None
    except Exception as e:
        messagebox.showerror('Error', f'Error reading file: {str(e)}')
        return None

# Function to handle button click for text files
def buttonClick(filePath):
    content = gettingFile(filePath)
    base_name = os.path.basename(filePath)  # Filename.txt
    title = os.path.splitext(base_name)[0]  # filename
    if content is not None:
        popupOnClick(content, title)  # for the title from text file

# Popup function
def popupOnClick(content, title):
    contentWindow = tk.Toplevel(guiAppWindow)
    contentWindow.title(title)  # title of window

    textArea = scrolledtext.ScrolledText(contentWindow, wrap=tk.WORD, width=100, height=30)  # Text area wrapping
    textArea.insert(tk.END, content)  # Text area inserting
    textArea.config(state=tk.DISABLED)  # Text area read-only
    textArea.pack(padx=10, pady=10)  # padding

# Main application window
guiAppWindow = tk.Tk()
guiAppWindow.title('Wordlist Resolver')
guiAppWindow.geometry("800x600")
guiAppWindow.configure(bg="#2e2e2e")

# Create a Canvas and a vertical scrollbar to enable scrolling
canvas = tk.Canvas(guiAppWindow, bg="#2e2e2e")
scrollbar = tk.Scrollbar(guiAppWindow, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#2e2e2e")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Layout the scrollbar and canvas
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# File Paths
filePaths = [
   # example file path r'XSS Burp payload.txt',
   ]

buttonNames = [
    "XSS payload",
    "SQLi – Payloads",
    "OS Command Injection Payload",
    "JAVA SCRIPT – Keywords to search in javascript file",
    "Tools for hacking",
    "NMAP CHEAT SHEET",
    "OPEN REDIRECT - Bypasses",
    "Sample Wordlist links",
    "IDOR",
    "SSRF – Filter Bypasses",
    "Sample Tool WorkFlows",
    "General Workflows"
]

# Create buttons for file paths with styles
leftSide = tk.Frame(scrollable_frame, bg="#2e2e2e")
rightBox = tk.Frame(scrollable_frame, bg="#2e2e2e")

for i, filePath in enumerate(filePaths):
    buttonName = buttonNames[i]
    button = tk.Button(leftSide if i % 2 == 0 else rightBox, text=buttonName, command=lambda fp=filePath: buttonClick(fp),
                       font=("Helvetica", 12), bg="#4caf50", fg="white", relief="raised", bd=3, padx=20, pady=10)
    button.pack(pady=10, padx=20)

leftSide.pack(side="left", fill="y", expand=True)
rightBox.pack(side="right", fill="y", expand=True)

# Start the application
guiAppWindow.mainloop()

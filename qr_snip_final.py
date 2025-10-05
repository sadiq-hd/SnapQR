import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import cv2
import webbrowser
import re

# ----- Detect & Decode QR -----
def decode_qr(image_path):
    try:
        img = cv2.imread(image_path)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        return data if data else "No QR code found."
    except Exception as e:
        return f"Error while reading QR: {e}"

# ----- Handle Image -----
def open_image():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if file_path:
        result = decode_qr(file_path)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)

        # Check if it's a valid URL → open automatically
        if re.match(r"^(https?://|www\.)", result.strip(), re.IGNORECASE):
            open_link(result.strip())
        else:
            messagebox.showinfo("QR Result", "Text copied below. You can copy it manually.")

# ----- Copy Text -----
def copy_result():
    text = entry_result.get().strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Result copied to clipboard.")
    else:
        messagebox.showwarning("Warning", "No text to copy!")

# ----- Open URL -----
def open_link(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        webbrowser.open_new(url)
    except Exception:
        messagebox.showerror("Error", "Failed to open the link.")

# ----- UI -----
root = tk.Tk()
root.title("SnapQR")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="SnapQR", font=("Segoe UI", 16, "bold")).pack(pady=10)

tk.Button(root, text="📂 Open Image", command=open_image, width=18).pack(pady=10)

tk.Label(root, text="Scan Result:", font=("Segoe UI", 10)).pack(pady=5)
entry_result = tk.Entry(root, width=50, justify="center")
entry_result.pack(pady=5)

tk.Button(root, text="📋 Copy Result", command=copy_result, width=18).pack(pady=10)

# LinkedIn footer
link = tk.Label(
    root,
    text="Developed by Sadiq Aldubaisi",
    fg="blue",
    cursor="hand2",
    font=("Segoe UI", 9, "italic"),
)
link.pack(pady=5)
link.bind("<Button-1>", lambda e: webbrowser.open_new(
    "https://www.linkedin.com/in/sadiq-aldubaisi-69721b222/"
))

root.mainloop()

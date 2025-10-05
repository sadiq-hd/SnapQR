import cv2
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pyzbar.pyzbar import decode
from PIL import ImageGrab, Image, ImageTk
import webbrowser

# ------------------------------------------------
# وظيفة قراءة الكود من الصورة
def scan_image(path):
    image = cv2.imread(path)
    barcodes = decode(image)
    if not barcodes:
        messagebox.showinfo("QR Snip", "لم يتم العثور على أي رمز QR أو باركود.")
        return
    text = "\n".join([b.data.decode("utf-8") for b in barcodes])
    result_text.set(text)

# وظيفة قراءة الكود من لقطة الشاشة
def scan_screenshot():
    messagebox.showinfo("QR Snip", "حدد الجزء الذي يحتوي على الكود ثم اضغط Enter.")
    img = ImageGrab.grabclipboard()
    if img is None:
        img = ImageGrab.grab()
    img.save("snip_temp.png")
    scan_image("snip_temp.png")

# فتح صورة من الجهاز
def open_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if path:
        scan_image(path)

# نسخ النتيجة
def copy_result():
    root.clipboard_clear()
    root.clipboard_append(result_text.get())
    messagebox.showinfo("نسخ", "تم نسخ النص بنجاح!")

# فتح حساب لينكدإن
def open_linkedin(event=None):
    webbrowser.open_new("https://www.linkedin.com/in/sadiq-aldubaisi")

# ------------------------------------------------
# واجهة المستخدم
root = tk.Tk()
root.title("QR Snip")
root.geometry("450x380")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

style = ttk.Style(root)
style.theme_use("clam")

ttk.Label(root, text="QR Snip", font=("Segoe UI", 18, "bold"), background="#f2f2f2").pack(pady=10)

btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="📁 فتح صورة", width=18, command=open_image).grid(row=0, column=0, padx=8)
ttk.Button(btn_frame, text="📸 لقطة شاشة", width=18, command=scan_screenshot).grid(row=0, column=1, padx=8)

ttk.Label(root, text="نتيجة القراءة:", background="#f2f2f2").pack(pady=(20, 5))
result_text = tk.StringVar()
text_box = tk.Entry(root, textvariable=result_text, font=("Segoe UI", 11), justify="center", width=45)
text_box.pack(ipady=5, padx=15)

ttk.Button(root, text="📋 نسخ النتيجة", command=copy_result).pack(pady=15)

footer = tk.Label(
    root,
    text="Developed by Sadiq Aldubaisi",
    fg="#0078D7",
    bg="#f2f2f2",
    font=("Segoe UI", 9, "bold"),
    cursor="hand2"
)
footer.pack(side="bottom", pady=8)
footer.bind("<Button-1>", open_linkedin)

root.mainloop()

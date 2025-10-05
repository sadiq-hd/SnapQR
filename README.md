# ⚡ SnapQR

**SnapQR** is a lightweight and modern QR Code Reader for Windows — built using **Python + OpenCV + Tkinter**.  
With just one click, you can open an image containing a QR code and instantly decode it.  
If the result is a **URL**, SnapQR opens it automatically in your browser; if it's **text**, you can simply copy it.

---

## 🎯 Features

- 🖼️ Load any QR code image (`.png`, `.jpg`, `.jpeg`, etc.)
- ⚙️ Automatically detects and decodes the QR content
- 🌐 Opens URLs directly in your browser
- 📋 Copies plain text QR content with one click
- 💡 Lightweight — No installation required
- 🧑‍💻 Developed by [Sadiq Aldubaisi](https://www.linkedin.com/in/sadiq-aldubaisi-69721b222/)

---

### 📦 Download Now  
➡️ [**Download SnapQR.exe**](https://github.com/sadiq-hd/SnapQR/releases/download/v1.0.0/SnapQR.exe)

---

## 🚀 How to Use

1. **Download** the latest `.exe` file from the [Releases page](../../releases)
2. Run `SnapQR.exe`
3. Click **Open Image** and choose your QR image  
   → If it’s a link, your browser will open automatically  
   → If it’s text, just hit **Copy Result**

---

## 🧩 Tech Stack

- **Python 3.13**
- **OpenCV**
- **Tkinter**
- **PyInstaller**

---

## 📦 Build Instructions (for developers)

To build the `.exe` yourself:

```bash
pip install pyinstaller opencv-python pillow
pyinstaller --onefile --windowed --icon="icon.ico" --name "SnapQR" qr_snip_final.py

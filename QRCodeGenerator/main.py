import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import os

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        # Entry and Button widgets
        self.label = tk.Label(root, text="Enter text or URL:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save QR Code", command=self.save_qr_code, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        # Image display area
        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack(pady=10)

        self.qr_image = None

    def generate_qr_code(self):
        # Get content from entry widget
        content = self.entry.get().strip()

        if content:
            # Generate QR code
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(content)
            qr.make(fit=True)

            # Create PIL image
            self.qr_image = qr.make_image(fill='black', back_color='white')

            # Display image on canvas
            self.display_qr_code()

            # Enable save button
            self.save_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Please enter text or URL.")

    def display_qr_code(self):
        # Convert PIL image to Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(self.qr_image)

        # Display image on canvas
        self.canvas.create_image(150, 150, image=tk_image)
        self.canvas.image = tk_image  # Keep reference to prevent garbage collection

    def save_qr_code(self):
        if self.qr_image:
            # Ask user to select directory to save the QR code image
            save_dir = filedialog.askdirectory()

            if save_dir:
                # Construct file path
                file_path = os.path.join(save_dir, "qrcode.png")

                # Save QR code image
                self.qr_image.save(file_path)
                messagebox.showinfo("Success", f"QR code saved successfully at:\n{file_path}")
        else:
            messagebox.showerror("Error", "No QR code generated yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
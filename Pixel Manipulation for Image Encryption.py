import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os
from pathlib import Path

class ImageEncryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Image Encryption Tool")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Variables
        self.original_image = None
        self.processed_image = None
        self.current_image_path = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main title
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(title_frame, text="🔐 Image Encryption Tool", 
                              font=('Arial', 24, 'bold'), 
                              fg='#ecf0f1', bg='#2c3e50')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Secure your images with pixel manipulation encryption", 
                                 font=('Arial', 12), 
                                 fg='#bdc3c7', bg='#2c3e50')
        subtitle_label.pack(pady=(5, 0))
        
        # Control panel
        control_frame = tk.Frame(self.root, bg='#34495e', relief='raised', bd=2)
        control_frame.pack(pady=20, padx=20, fill='x')
        
        # File selection
        file_frame = tk.Frame(control_frame, bg='#34495e')
        file_frame.pack(pady=15, padx=20, fill='x')
        
        tk.Label(file_frame, text="📁 Select Image:", 
                font=('Arial', 12, 'bold'), 
                fg='#ecf0f1', bg='#34495e').pack(anchor='w')
        
        file_button_frame = tk.Frame(file_frame, bg='#34495e')
        file_button_frame.pack(fill='x', pady=(5, 0))
        
        self.select_btn = tk.Button(file_button_frame, text="Browse Image", 
                                   command=self.select_image,
                                   bg='#3498db', fg='white', 
                                   font=('Arial', 10, 'bold'),
                                   relief='flat', padx=20, pady=5,
                                   cursor='hand2')
        self.select_btn.pack(side='left')
        
        self.file_label = tk.Label(file_button_frame, text="No file selected", 
                                  font=('Arial', 10), 
                                  fg='#bdc3c7', bg='#34495e')
        self.file_label.pack(side='left', padx=(10, 0))
        
        # Encryption key
        key_frame = tk.Frame(control_frame, bg='#34495e')
        key_frame.pack(pady=15, padx=20, fill='x')
        
        tk.Label(key_frame, text="🔑 Encryption Key (1-255):", 
                font=('Arial', 12, 'bold'), 
                fg='#ecf0f1', bg='#34495e').pack(anchor='w')
        
        key_input_frame = tk.Frame(key_frame, bg='#34495e')
        key_input_frame.pack(fill='x', pady=(5, 0))
        
        self.key_var = tk.StringVar(value="50")
        self.key_entry = tk.Entry(key_input_frame, textvariable=self.key_var,
                                 font=('Arial', 11), width=10,
                                 relief='flat', bd=5)
        self.key_entry.pack(side='left')
        
        # Action buttons
        button_frame = tk.Frame(control_frame, bg='#34495e')
        button_frame.pack(pady=15, padx=20)
        
        self.encrypt_btn = tk.Button(button_frame, text="🔒 Encrypt Image", 
                                    command=self.encrypt_image,
                                    bg='#e74c3c', fg='white', 
                                    font=('Arial', 11, 'bold'),
                                    relief='flat', padx=20, pady=8,
                                    cursor='hand2', state='disabled')
        self.encrypt_btn.pack(side='left', padx=(0, 10))
        
        self.decrypt_btn = tk.Button(button_frame, text="🔓 Decrypt Image", 
                                    command=self.decrypt_image,
                                    bg='#27ae60', fg='white', 
                                    font=('Arial', 11, 'bold'),
                                    relief='flat', padx=20, pady=8,
                                    cursor='hand2', state='disabled')
        self.decrypt_btn.pack(side='left', padx=(0, 10))
        
        self.save_btn = tk.Button(button_frame, text="💾 Save Result", 
                                 command=self.save_image,
                                 bg='#f39c12', fg='white', 
                                 font=('Arial', 11, 'bold'),
                                 relief='flat', padx=20, pady=8,
                                 cursor='hand2', state='disabled')
        self.save_btn.pack(side='left')
        
        # Image display area
        image_frame = tk.Frame(self.root, bg='#2c3e50')
        image_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Before and After frames
        self.before_frame = tk.LabelFrame(image_frame, text="Original Image", 
                                         font=('Arial', 12, 'bold'),
                                         fg='#ecf0f1', bg='#34495e',
                                         relief='raised', bd=2)
        self.before_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        self.before_label = tk.Label(self.before_frame, text="No image selected", 
                                    font=('Arial', 14), 
                                    fg='#bdc3c7', bg='#34495e')
        self.before_label.pack(expand=True)
        
        self.after_frame = tk.LabelFrame(image_frame, text="Processed Image", 
                                        font=('Arial', 12, 'bold'),
                                        fg='#ecf0f1', bg='#34495e',
                                        relief='raised', bd=2)
        self.after_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        self.after_label = tk.Label(self.after_frame, text="Process an image", 
                                   font=('Arial', 14), 
                                   fg='#bdc3c7', bg='#34495e')
        self.after_label.pack(expand=True)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to encrypt/decrypt images")
        status_bar = tk.Label(self.root, textvariable=self.status_var,
                             font=('Arial', 10), 
                             fg='#ecf0f1', bg='#2c3e50',
                             relief='sunken', anchor='w')
        status_bar.pack(side='bottom', fill='x')
        
    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff *.gif"),
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.original_image = Image.open(file_path)
                self.current_image_path = file_path
                
                # Display original image
                self.display_image(self.original_image, self.before_label)
                
                # Update UI
                self.file_label.config(text=os.path.basename(file_path))
                self.encrypt_btn.config(state='normal')
                self.decrypt_btn.config(state='normal')
                self.status_var.set(f"Image loaded: {os.path.basename(file_path)}")
                
                # Clear processed image
                self.after_label.config(image='', text="Process an image")
                self.processed_image = None
                self.save_btn.config(state='disabled')
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
                self.status_var.set("Error loading image")
    
    def display_image(self, image, label):
        # Resize image to fit display
        display_size = (250, 200)
        image_copy = image.copy()
        image_copy.thumbnail(display_size, Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage
        photo = ImageTk.PhotoImage(image_copy)
        label.config(image=photo, text='')
        label.image = photo  # Keep a reference
    
    def validate_key(self):
        try:
            key = int(self.key_var.get())
            if 1 <= key <= 255:
                return key
            else:
                messagebox.showerror("Invalid Key", "Key must be between 1 and 255")
                return None
        except ValueError:
            messagebox.showerror("Invalid Key", "Key must be a valid number")
            return None
    
    def encrypt_image(self):
        if not self.original_image:
            messagebox.showwarning("No Image", "Please select an image first")
            return
        
        key = self.validate_key()
        if key is None:
            return
        
        try:
            self.status_var.set("Encrypting image...")
            self.root.update()
            
            # Convert to RGB if necessary
            if self.original_image.mode != 'RGB':
                img_rgb = self.original_image.convert('RGB')
            else:
                img_rgb = self.original_image.copy()
            
            # Convert to numpy array
            img_array = np.array(img_rgb)
            
            # Encrypt by adding key to each pixel value
            encrypted_array = (img_array.astype(np.int16) + key) % 256
            encrypted_array = encrypted_array.astype(np.uint8)
            
            # Convert back to PIL Image
            self.processed_image = Image.fromarray(encrypted_array, 'RGB')
            
            # Display encrypted image
            self.display_image(self.processed_image, self.after_label)
            
            # Update UI
            self.save_btn.config(state='normal')
            self.after_frame.config(text="Encrypted Image")
            self.status_var.set(f"Image encrypted with key: {key}")
            
        except Exception as e:
            messagebox.showerror("Encryption Error", f"Failed to encrypt image: {str(e)}")
            self.status_var.set("Encryption failed")
    
    def decrypt_image(self):
        if not self.original_image:
            messagebox.showwarning("No Image", "Please select an image first")
            return
        
        key = self.validate_key()
        if key is None:
            return
        
        try:
            self.status_var.set("Decrypting image...")
            self.root.update()
            
            # Convert to RGB if necessary
            if self.original_image.mode != 'RGB':
                img_rgb = self.original_image.convert('RGB')
            else:
                img_rgb = self.original_image.copy()
            
            # Convert to numpy array
            img_array = np.array(img_rgb)
            
            # Decrypt by subtracting key from each pixel value
            decrypted_array = (img_array.astype(np.int16) - key) % 256
            decrypted_array = decrypted_array.astype(np.uint8)
            
            # Convert back to PIL Image
            self.processed_image = Image.fromarray(decrypted_array, 'RGB')
            
            # Display decrypted image
            self.display_image(self.processed_image, self.after_label)
            
            # Update UI
            self.save_btn.config(state='normal')
            self.after_frame.config(text="Decrypted Image")
            self.status_var.set(f"Image decrypted with key: {key}")
            
        except Exception as e:
            messagebox.showerror("Decryption Error", f"Failed to decrypt image: {str(e)}")
            self.status_var.set("Decryption failed")
    
    def save_image(self):
        if not self.processed_image:
            messagebox.showwarning("No Processed Image", "No processed image to save")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save Processed Image",
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.processed_image.save(file_path)
                messagebox.showinfo("Success", f"Image saved successfully to:\n{file_path}")
                self.status_var.set(f"Image saved: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Save Error", f"Failed to save image: {str(e)}")
                self.status_var.set("Failed to save image")

def main():
    root = tk.Tk()
    app = ImageEncryptionTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
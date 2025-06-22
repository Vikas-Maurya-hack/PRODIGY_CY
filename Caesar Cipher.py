import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import string

class CaesarCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher - Encrypt & Decrypt")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Set up the visual styling first
        self.setup_styles()
        
        # Create the main container
        main_frame = tk.Frame(root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Add the title at the top
        title_label = tk.Label(main_frame, text="Caesar Cipher Tool", 
                              font=('Arial', 24, 'bold'), 
                              fg='#ecf0f1', bg='#2c3e50')
        title_label.pack(pady=(0, 20))
        
        # Build the interface sections
        self.create_input_section(main_frame)
        self.create_controls_section(main_frame)
        self.create_output_section(main_frame)
        self.create_file_section(main_frame)
        self.create_status_bar(main_frame)
        
    def setup_styles(self):
        # Configure the look and feel of our widgets
        style = ttk.Style()
        
        # Try to use a nice theme, but don't break if it's not available
        try:
            style.theme_use('clam')
        except:
            pass  # Just use whatever theme is default
        
        # Make our buttons look modern and blue
        style.configure('Modern.TButton',
                       borderwidth=1,
                       focuscolor='none',
                       background='#3498db',
                       foreground='white',
                       font=('Arial', 10, 'bold'))
        
        # Button hover effects
        style.map('Modern.TButton',
                 background=[('active', '#2980b9'),
                           ('pressed', '#21618c')])
        
        # Style the slider to match our dark theme
        style.configure('TScale',
                       background='#2c3e50',
                       troughcolor='#34495e')
    
    def create_input_section(self, parent):
        # This is where users will type or paste their text
        input_frame = tk.Frame(parent, bg='#2c3e50')
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(input_frame, text="Input Text:", 
                font=('Arial', 12, 'bold'), 
                fg='#ecf0f1', bg='#2c3e50').pack(anchor='w')
        
        # Create a frame to hold the text area and scrollbar
        text_frame = tk.Frame(input_frame, bg='#2c3e50')
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Main text input area
        self.input_text = tk.Text(text_frame, height=6, 
                                 font=('Consolas', 11),
                                 bg='#ecf0f1', fg='#2c3e50',
                                 insertbackground='#2c3e50',
                                 relief='flat', borderwidth=2)
        
        # Add a scrollbar in case of long text
        input_scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, 
                                       command=self.input_text.yview)
        self.input_text.configure(yscrollcommand=input_scrollbar.set)
        
        self.input_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add some helpful placeholder text
        self.input_text.insert('1.0', "Enter your text here to encrypt or decrypt...")
        self.input_text.bind('<FocusIn>', self.clear_placeholder)
        self.input_text.bind('<FocusOut>', self.add_placeholder)
        
    def create_controls_section(self, parent):
        # This section has the shift value control and action buttons
        controls_frame = tk.Frame(parent, bg='#2c3e50')
        controls_frame.pack(fill=tk.X, pady=15)
        
        # Left side: shift value controls
        shift_frame = tk.Frame(controls_frame, bg='#2c3e50')
        shift_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(shift_frame, text="Shift Value:", 
                font=('Arial', 12, 'bold'), 
                fg='#ecf0f1', bg='#2c3e50').pack(anchor='w')
        
        shift_control_frame = tk.Frame(shift_frame, bg='#2c3e50')
        shift_control_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Show the current shift value prominently
        self.shift_var = tk.IntVar(value=3)  # Start with a common shift value
        self.shift_label = tk.Label(shift_control_frame, 
                                   textvariable=self.shift_var,
                                   font=('Arial', 14, 'bold'),
                                   fg='#3498db', bg='#2c3e50',
                                   width=3)
        self.shift_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Slider to adjust the shift value
        self.shift_scale = ttk.Scale(shift_control_frame, 
                                   from_=1, to=25,
                                   orient=tk.HORIZONTAL,
                                   variable=self.shift_var,
                                   command=self.update_shift_display)
        self.shift_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Right side: action buttons
        buttons_frame = tk.Frame(controls_frame, bg='#2c3e50')
        buttons_frame.pack(side=tk.RIGHT, padx=(20, 0))
        
        # Main action buttons with icons for visual appeal
        self.encrypt_btn = ttk.Button(buttons_frame, text="🔒 Encrypt", 
                                    command=self.encrypt_text,
                                    style='Modern.TButton',
                                    width=12)
        self.encrypt_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.decrypt_btn = ttk.Button(buttons_frame, text="🔓 Decrypt", 
                                    command=self.decrypt_text,
                                    style='Modern.TButton',
                                    width=12)
        self.decrypt_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Utility button to clear everything
        self.clear_btn = ttk.Button(buttons_frame, text="🗑️ Clear", 
                                  command=self.clear_all,
                                  style='Modern.TButton',
                                  width=10)
        self.clear_btn.pack(side=tk.LEFT)
        
    def create_output_section(self, parent):
        # Where the encrypted/decrypted results appear
        output_frame = tk.Frame(parent, bg='#2c3e50')
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(15, 0))
        
        # Header with copy button for convenience
        output_header = tk.Frame(output_frame, bg='#2c3e50')
        output_header.pack(fill=tk.X)
        
        tk.Label(output_header, text="Output Text:", 
                font=('Arial', 12, 'bold'), 
                fg='#ecf0f1', bg='#2c3e50').pack(side=tk.LEFT)
        
        ttk.Button(output_header, text="📋 Copy", 
                  command=self.copy_output,
                  style='Modern.TButton',
                  width=8).pack(side=tk.RIGHT)
        
        # Output text area (read-only)
        text_frame = tk.Frame(output_frame, bg='#2c3e50')
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        self.output_text = tk.Text(text_frame, height=6, 
                                  font=('Consolas', 11),
                                  bg='#ecf0f1', fg='#2c3e50',
                                  relief='flat', borderwidth=2,
                                  state='disabled')  # Read-only by default
        
        output_scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, 
                                        command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=output_scrollbar.set)
        
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def create_file_section(self, parent):
        # File operations for loading and saving text
        file_frame = tk.Frame(parent, bg='#2c3e50')
        file_frame.pack(fill=tk.X, pady=(15, 0))
        
        tk.Label(file_frame, text="File Operations:", 
                font=('Arial', 12, 'bold'), 
                fg='#ecf0f1', bg='#2c3e50').pack(anchor='w')
        
        file_buttons_frame = tk.Frame(file_frame, bg='#2c3e50')
        file_buttons_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Button(file_buttons_frame, text="📁 Load File", 
                  command=self.load_file,
                  style='Modern.TButton',
                  width=12).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(file_buttons_frame, text="💾 Save Output", 
                  command=self.save_file,
                  style='Modern.TButton',
                  width=12).pack(side=tk.LEFT)
        
    def create_status_bar(self, parent):
        # Status bar to show what's happening
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(parent, textvariable=self.status_var,
                             relief=tk.SUNKEN, anchor=tk.W,
                             bg='#34495e', fg='#ecf0f1',
                             font=('Arial', 9))
        status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        
    def update_shift_display(self, value):
        # Update the shift value display when slider moves
        self.shift_var.set(int(float(value)))
        
    def clear_placeholder(self, event):
        # Remove placeholder text when user clicks in the input area
        if self.input_text.get('1.0', tk.END).strip() == "Enter your text here to encrypt or decrypt...":
            self.input_text.delete('1.0', tk.END)
            
    def add_placeholder(self, event):
        # Put placeholder text back if the input area is empty
        if not self.input_text.get('1.0', tk.END).strip():
            self.input_text.insert('1.0', "Enter your text here to encrypt or decrypt...")
            
    def caesar_cipher(self, text, shift, decrypt=False):
        # The core Caesar cipher algorithm
        if decrypt:
            shift = -shift  # Reverse the shift for decryption
            
        result = []
        for char in text:
            if char.isalpha():
                # Handle both uppercase and lowercase letters
                is_upper = char.isupper()
                char = char.lower()
                
                # Apply the Caesar shift
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                
                # Preserve the original case
                if is_upper:
                    shifted = shifted.upper()
                    
                result.append(shifted)
            else:
                # Keep non-alphabetic characters unchanged
                result.append(char)
                
        return ''.join(result)
    
    def encrypt_text(self):
        # Handle the encrypt button click
        input_content = self.input_text.get('1.0', tk.END).strip()
        
        # Make sure there's actually text to encrypt
        if not input_content or input_content == "Enter your text here to encrypt or decrypt...":
            messagebox.showwarning("Warning", "Please enter text to encrypt!")
            return
            
        try:
            shift = self.shift_var.get()
            encrypted = self.caesar_cipher(input_content, shift)
            
            # Show the encrypted result
            self.output_text.config(state='normal')
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert('1.0', encrypted)
            self.output_text.config(state='disabled')
            
            self.status_var.set(f"Text encrypted with shift {shift}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")
            
    def decrypt_text(self):
        # Handle the decrypt button click
        input_content = self.input_text.get('1.0', tk.END).strip()
        
        # Make sure there's text to decrypt
        if not input_content or input_content == "Enter your text here to encrypt or decrypt...":
            messagebox.showwarning("Warning", "Please enter text to decrypt!")
            return
            
        try:
            shift = self.shift_var.get()
            decrypted = self.caesar_cipher(input_content, shift, decrypt=True)
            
            # Show the decrypted result
            self.output_text.config(state='normal')
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert('1.0', decrypted)
            self.output_text.config(state='disabled')
            
            self.status_var.set(f"Text decrypted with shift {shift}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")
            
    def clear_all(self):
        # Reset everything back to empty state
        self.input_text.delete('1.0', tk.END)
        self.add_placeholder(None)
        
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state='disabled')
        
        self.status_var.set("Cleared all text")
        
    def copy_output(self):
        # Copy the output text to the clipboard for easy pasting
        output_content = self.output_text.get('1.0', tk.END).strip()
        
        if output_content:
            self.root.clipboard_clear()
            self.root.clipboard_append(output_content)
            self.status_var.set("Output copied to clipboard")
        else:
            messagebox.showinfo("Info", "No output text to copy!")
            
    def load_file(self):
        # Let the user select and load a text file
        file_path = filedialog.askopenfilename(
            title="Select text file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                # Put the file content into the input area
                self.input_text.delete('1.0', tk.END)
                self.input_text.insert('1.0', content)
                
                self.status_var.set(f"Loaded file: {file_path}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {str(e)}")
                
    def save_file(self):
        # Save the output text to a file
        output_content = self.output_text.get('1.0', tk.END).strip()
        
        if not output_content:
            messagebox.showwarning("Warning", "No output text to save!")
            return
            
        file_path = filedialog.asksaveasfilename(
            title="Save output text",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(output_content)
                    
                self.status_var.set(f"Saved to: {file_path}")
                messagebox.showinfo("Success", "Output saved successfully!")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def main():
    # Set up and run the main application
    root = tk.Tk()
    app = CaesarCipherGUI(root)
    
    # Center the window on the screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    # Set minimum window size but allow resizing
    root.minsize(600, 500)
    
    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
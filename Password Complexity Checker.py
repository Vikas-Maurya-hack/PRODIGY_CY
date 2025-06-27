import tkinter as tk
from tkinter import ttk, messagebox
import re
import string

class PasswordComplexityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Complexity Checker")
        self.root.geometry("500x650")
        self.root.configure(bg='#f0f0f0')
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="Password Complexity Checker", 
                              font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=(0, 20))
        
        # Password input frame
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(input_frame, text="Enter Password:", font=('Arial', 12)).pack(anchor=tk.W)
        
        # Password entry with show/hide functionality
        self.password_var = tk.StringVar()
        self.password_var.trace('w', self.on_password_change)
        
        entry_frame = ttk.Frame(input_frame)
        entry_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.password_entry = ttk.Entry(entry_frame, textvariable=self.password_var, 
                                       font=('Arial', 12), show='*')
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.show_password = tk.BooleanVar()
        self.show_checkbox = ttk.Checkbutton(entry_frame, text="Show", 
                                           variable=self.show_password,
                                           command=self.toggle_password_visibility)
        self.show_checkbox.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Strength indicator
        strength_frame = ttk.Frame(main_frame)
        strength_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(strength_frame, text="Password Strength:", font=('Arial', 12, 'bold')).pack(anchor=tk.W)
        
        self.strength_label = tk.Label(strength_frame, text="Enter a password to check", 
                                      font=('Arial', 11), bg='#f0f0f0')
        self.strength_label.pack(anchor=tk.W, pady=(5, 0))
        
        # Progress bar for strength
        self.strength_progress = ttk.Progressbar(strength_frame, length=300, mode='determinate')
        self.strength_progress.pack(fill=tk.X, pady=(5, 0))
        
        # Criteria checklist
        criteria_frame = ttk.LabelFrame(main_frame, text="Password Criteria", padding="15")
        criteria_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.criteria_labels = {}
        criteria_list = [
            ("length", "At least 8 characters"),
            ("uppercase", "Contains uppercase letters (A-Z)"),
            ("lowercase", "Contains lowercase letters (a-z)"),
            ("numbers", "Contains numbers (0-9)"),
            ("special", "Contains special characters (!@#$%^&*)")
        ]
        
        for key, text in criteria_list:
            frame = ttk.Frame(criteria_frame)
            frame.pack(fill=tk.X, pady=2)
            
            self.criteria_labels[key] = tk.Label(frame, text=f"✗ {text}", 
                                               font=('Arial', 10), fg='red', bg='#f0f0f0')
            self.criteria_labels[key].pack(anchor=tk.W)
        
        # Score frame
        score_frame = ttk.LabelFrame(main_frame, text="Detailed Analysis", padding="15")
        score_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.score_text = tk.Text(score_frame, height=6, width=50, font=('Arial', 10),
                                 bg='#ffffff', fg='#333', wrap=tk.WORD, state=tk.DISABLED,
                                 relief=tk.FLAT, borderwidth=1)
        self.score_text.pack(fill=tk.X, expand=False)
        
        # Suggestions frame
        suggestions_frame = ttk.LabelFrame(main_frame, text="Suggestions", padding="15")
        suggestions_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.suggestions_text = tk.Text(suggestions_frame, height=5, width=50, font=('Arial', 10),
                                       bg='#ffffff', fg='#333', wrap=tk.WORD, state=tk.DISABLED,
                                       relief=tk.FLAT, borderwidth=1)
        self.suggestions_text.pack(fill=tk.X, expand=False)
        
        # Generate password button
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=(10, 0))
        
        generate_btn = ttk.Button(button_frame, text="Generate Strong Password", 
                                 command=self.generate_password)
        generate_btn.pack()
        
        # Initialize with empty password
        self.check_password("")
    
    def toggle_password_visibility(self):
        if self.show_password.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
    
    def on_password_change(self, *args):
        password = self.password_var.get()
        self.check_password(password)
    
    def check_password(self, password):
        if not password:
            self.reset_display()
            return
        
        # Check criteria
        criteria_results = {
            'length': len(password) >= 8,
            'uppercase': bool(re.search(r'[A-Z]', password)),
            'lowercase': bool(re.search(r'[a-z]', password)),
            'numbers': bool(re.search(r'[0-9]', password)),
            'special': bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]', password))
        }
        
        # Update criteria display
        for key, result in criteria_results.items():
            if result:
                self.criteria_labels[key].config(text=f"✓ {self.criteria_labels[key].cget('text')[2:]}", 
                                               fg='green')
            else:
                self.criteria_labels[key].config(text=f"✗ {self.criteria_labels[key].cget('text')[2:]}", 
                                               fg='red')
        
        # Calculate strength
        strength_score = sum(criteria_results.values())
        strength_percentage = (strength_score / 5) * 100
        
        # Additional scoring factors
        length_bonus = min((len(password) - 8) * 2, 10) if len(password) > 8 else 0
        variety_bonus = len(set(password)) * 0.5
        
        total_score = min(strength_percentage + length_bonus + variety_bonus, 100)
        
        # Update strength display
        self.update_strength_display(total_score, strength_score)
        
        # Update detailed analysis
        self.update_analysis(password, criteria_results, total_score)
        
        # Update suggestions
        self.update_suggestions(criteria_results, password)
    
    def update_strength_display(self, score, criteria_met):
        self.strength_progress['value'] = score
        
        if score < 30:
            strength_text = "Very Weak"
            color = "#ff4444"
        elif score < 50:
            strength_text = "Weak"
            color = "#ff8800"
        elif score < 70:
            strength_text = "Fair"
            color = "#ffcc00"
        elif score < 85:
            strength_text = "Good"
            color = "#88cc00"
        else:
            strength_text = "Strong"
            color = "#00cc44"
        
        self.strength_label.config(text=f"{strength_text} ({score:.0f}%)", fg=color)
    
    def update_analysis(self, password, criteria_results, score):
        self.score_text.config(state=tk.NORMAL)
        self.score_text.delete(1.0, tk.END)
        
        analysis = f"Password Length: {len(password)} characters\n"
        analysis += f"Criteria Met: {sum(criteria_results.values())}/5\n"
        analysis += f"Overall Score: {score:.0f}%\n"
        analysis += f"Unique Characters: {len(set(password))}\n"
        
        if password:
            char_types = []
            if any(c.isupper() for c in password):
                char_types.append("Uppercase")
            if any(c.islower() for c in password):
                char_types.append("Lowercase")
            if any(c.isdigit() for c in password):
                char_types.append("Numbers")
            if any(c in string.punctuation for c in password):
                char_types.append("Special")
            
            analysis += f"Character Types: {', '.join(char_types)}\n"
        
        self.score_text.insert(tk.END, analysis)
        self.score_text.config(state=tk.DISABLED)
    
    def update_suggestions(self, criteria_results, password):
        self.suggestions_text.config(state=tk.NORMAL)
        self.suggestions_text.delete(1.0, tk.END)
        
        suggestions = []
        
        if not criteria_results['length']:
            suggestions.append("• Add more characters (minimum 8)")
        
        if not criteria_results['uppercase']:
            suggestions.append("• Include uppercase letters (A-Z)")
        
        if not criteria_results['lowercase']:
            suggestions.append("• Include lowercase letters (a-z)")
        
        if not criteria_results['numbers']:
            suggestions.append("• Include numbers (0-9)")
        
        if not criteria_results['special']:
            suggestions.append("• Include special characters (!@#$%^&*)")
        
        if len(password) < 12:
            suggestions.append("• Consider using 12+ characters for better security")
        
        if len(set(password)) < len(password) * 0.7:
            suggestions.append("• Avoid repeating characters too frequently")
        
        if not suggestions:
            suggestions.append("• Great! Your password meets all criteria")
            suggestions.append("• For maximum security, use 16+ characters")
            suggestions.append("• Avoid using personal information")
        
        self.suggestions_text.insert(tk.END, "\n".join(suggestions))
        self.suggestions_text.config(state=tk.DISABLED)
    
    def generate_password(self):
        import random
        
        # Character sets
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        numbers = string.digits
        special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Ensure at least one character from each set
        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(numbers),
            random.choice(special)
        ]
        
        # Fill remaining positions
        all_chars = uppercase + lowercase + numbers + special
        for _ in range(8):  # Generate 12 character password
            password.append(random.choice(all_chars))
        
        # Shuffle the password
        random.shuffle(password)
        generated_password = ''.join(password)
        
        # Set the generated password
        self.password_var.set(generated_password)
        
        # Show message
        messagebox.showinfo("Password Generated", 
                           f"Strong password generated!\n\nPassword: {generated_password}")
    
    def reset_display(self):
        self.strength_label.config(text="Enter a password to check", fg='black')
        self.strength_progress['value'] = 0
        
        # Reset criteria
        criteria_texts = [
            "At least 8 characters",
            "Contains uppercase letters (A-Z)",
            "Contains lowercase letters (a-z)",
            "Contains numbers (0-9)",
            "Contains special characters (!@#$%^&*)"
        ]
        
        for i, (key, _) in enumerate([
            ("length", ""), ("uppercase", ""), ("lowercase", ""), ("numbers", ""), ("special", "")
        ]):
            self.criteria_labels[key].config(text=f"✗ {criteria_texts[i]}", fg='red')
        
        # Clear text areas
        self.score_text.config(state=tk.NORMAL)
        self.score_text.delete(1.0, tk.END)
        self.score_text.insert(tk.END, "Enter a password to see detailed analysis...")
        self.score_text.config(state=tk.DISABLED)
        
        self.suggestions_text.config(state=tk.NORMAL)
        self.suggestions_text.delete(1.0, tk.END)
        self.suggestions_text.insert(tk.END, "Suggestions will appear here...")
        self.suggestions_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = PasswordComplexityChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
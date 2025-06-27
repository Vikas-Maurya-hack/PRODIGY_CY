# Password Complexity Checker

A user-friendly GUI application built with Python that evaluates password strength based on common security criteria. The tool provides real-time feedback, detailed analysis, and suggestions for creating stronger passwords.

## Features

### 🔐 Password Evaluation
- **Real-time analysis** as you type
- **Visual strength indicator** with progress bar
- **Color-coded feedback** (Very Weak to Strong)
- **Comprehensive scoring system** (0-100%)

### 📋 Security Criteria Checked
- ✅ **Length**: Minimum 8 characters
- ✅ **Uppercase letters**: A-Z
- ✅ **Lowercase letters**: a-z  
- ✅ **Numbers**: 0-9
- ✅ **Special characters**: !@#$%^&*()_+-=[]{}|;:,.<>?

### 🔍 Detailed Analysis
- Character count and types
- Unique character analysis
- Criteria compliance summary
- Overall security score

### 💡 Smart Suggestions
- Personalized recommendations
- Security best practices
- Tips for improvement

### 🎯 Additional Features
- **Show/Hide password** toggle
- **Strong password generator**
- **User-friendly interface**
- **Real-time updates**

## Screenshots

The application features a clean, intuitive interface with:
- Password input field with visibility toggle
- Visual strength meter
- Criteria checklist with checkmarks
- Detailed analysis panel
- Suggestion box
- Password generator button

## Requirements

### System Requirements
- **Python**: 3.6 or higher
- **Operating System**: Windows, macOS, or Linux

### Dependencies
- `tkinter` (usually included with Python)
- `re` (built-in module)
- `string` (built-in module)
- `random` (built-in module)

*Note: All dependencies are part of Python's standard library, so no additional installations are required!*

## Installation & Setup

### Method 1: Direct Download
1. Download the `password_checker.py` file
2. Save it to your desired directory
3. Run the application (see Usage section)

### Method 2: Clone Repository
```bash
git clone <repository-url>
cd password-complexity-checker
```

## Usage

### Running the Application

#### From Command Line:
```bash
python password_checker.py
```

#### From Python IDE:
1. Open `password_checker.py` in your preferred Python IDE
2. Run the script (F5 in most IDEs)

#### Double-click (Windows):
- If Python is properly configured, you can double-click the `.py` file

### How to Use

1. **Enter Password**: Type your password in the input field
2. **View Analysis**: Watch real-time feedback as you type
3. **Check Criteria**: See which security requirements are met
4. **Read Suggestions**: Follow recommendations to improve strength
5. **Generate Password**: Click "Generate Strong Password" for a secure option
6. **Toggle Visibility**: Use the "Show" checkbox to reveal/hide password

## Password Strength Levels

| Score Range | Strength Level | Color Code |
|-------------|---------------|------------|
| 0-29%       | Very Weak     | 🔴 Red     |
| 30-49%      | Weak          | 🟠 Orange  |
| 50-69%      | Fair          | 🟡 Yellow  |
| 70-84%      | Good          | 🟢 Light Green |
| 85-100%     | Strong        | 🟢 Green   |

## Scoring Algorithm

The application uses a comprehensive scoring system:

### Base Score (0-100%)
- **5 Criteria**: Each criterion contributes 20% when met
  - Length ≥ 8 characters (20%)
  - Uppercase letters (20%)
  - Lowercase letters (20%)
  - Numbers (20%)
  - Special characters (20%)

### Bonus Points
- **Length Bonus**: +2% for each character beyond 8 (max +10%)
- **Variety Bonus**: +0.5% for each unique character
- **Maximum Score**: Capped at 100%

## Security Best Practices

### ✅ Do's
- Use at least 12-16 characters
- Include all character types
- Use unique passwords for each account
- Consider using a password manager
- Update passwords regularly

### ❌ Don'ts
- Don't use personal information
- Avoid common words or patterns
- Don't reuse passwords
- Avoid predictable substitutions (@ for a, 3 for e)
- Don't share passwords

## Customization

### Modifying Criteria
To adjust password requirements, edit the `check_password` method:

```python
criteria_results = {
    'length': len(password) >= 12,  # Change minimum length
    'uppercase': bool(re.search(r'[A-Z]', password)),
    # Add more criteria as needed
}
```

### Changing Appearance
Modify colors and fonts in the `__init__` method:

```python
# Change colors
title_label = tk.Label(main_frame, text="Password Complexity Checker", 
                      font=('Arial', 18, 'bold'), 
                      bg='#your_color', fg='#text_color')
```

### Adding New Features
The modular design makes it easy to add:
- Password history tracking
- Export functionality
- Different strength algorithms
- Custom dictionaries for common passwords

## Troubleshooting

### Common Issues

**Issue**: Application won't start
- **Solution**: Ensure Python 3.6+ is installed and tkinter is available

**Issue**: Interface appears distorted
- **Solution**: Try running on a different display resolution or update tkinter

**Issue**: Generate button not working
- **Solution**: Check that the `random` module is available

### Getting Help

If you encounter issues:
1. Check that all dependencies are installed
2. Verify Python version compatibility
3. Try running from command line to see error messages
4. Check for typos if you modified the code

## Contributing

Contributions are welcome! You can help by:
- Reporting bugs
- Suggesting new features
- Improving documentation
- Adding security enhancements
- Creating tests

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with Python's tkinter for cross-platform compatibility
- Inspired by modern password security standards
- Thanks to the Python community for excellent documentation

---

**Happy Password Checking! 🔐**

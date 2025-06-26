# 🔐 Image Encryption Tool

A simple yet powerful GUI-based image encryption tool that uses pixel manipulation techniques to secure your images. This tool demonstrates the basics of image encryption and serves as a foundation for understanding image steganography and data hiding concepts.

<img width="959" alt="image" src="https://github.com/user-attachments/assets/e27257f0-0e43-4296-9fd3-ec165bdb755c" />


## 🌟 Features

- **Simple Pixel Manipulation Encryption**: Uses RGB value shifting for encryption/decryption
- **User-Friendly GUI**: Clean, modern interface built with Tkinter
- **Multiple Image Formats**: Supports PNG, JPEG, BMP, TIFF, and GIF
- **Real-time Preview**: Side-by-side comparison of original and processed images
- **Customizable Encryption Key**: Choose any key between 1-255
- **Save Functionality**: Export encrypted/decrypted images in various formats

## 📸 Screenshots

### Main Interface
The tool features a clean, dark-themed interface with easy-to-use controls:

- **File Selection**: Browse and select images to encrypt/decrypt
- **Key Input**: Enter encryption key (1-255)
- **Action Buttons**: Encrypt, decrypt, and save operations
- **Image Preview**: Side-by-side view of original and processed images

## 🚀 How It Works

### Encryption Process
1. **Load Image**: The tool converts the image to RGB format
2. **Pixel Manipulation**: Adds the encryption key to each pixel's RGB values
3. **Modulo Operation**: Uses modulo 256 to keep values within valid range (0-255)
4. **Result**: Creates an encrypted image that looks like random noise

### Decryption Process
1. **Load Encrypted Image**: Load the previously encrypted image
2. **Reverse Operation**: Subtracts the same encryption key from pixel values
3. **Modulo Operation**: Ensures values stay within valid range
4. **Result**: Recovers the original image (if correct key is used)

### Mathematical Formula
```
Encryption: Encrypted_Pixel = (Original_Pixel + Key) % 256
Decryption: Original_Pixel = (Encrypted_Pixel - Key) % 256
```

## 📋 Requirements

- Python 3.7 or higher
- Pillow (PIL) for image processing
- NumPy for array operations
- Tkinter (usually comes with Python)

## 🛠️ Installation

### Option 1: Clone from GitHub
```bash
git clone https://github.com/yourusername/image-encryption-tool.git
cd image-encryption-tool
pip install -r requirements.txt
python image_encryption_tool.py
```

### Option 2: Download ZIP
1. Download the ZIP file from GitHub
2. Extract to your desired location
3. Open terminal/command prompt in the extracted folder
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python image_encryption_tool.py
   ```

## 🎯 Usage Guide

### Step 1: Launch the Application
```bash
python image_encryption_tool.py
```

### Step 2: Select an Image
- Click "Browse Image" button
- Choose any supported image file (PNG, JPEG, BMP, TIFF, GIF)
- The image will appear in the "Original Image" panel

### Step 3: Set Encryption Key
- Enter a number between 1-255 in the "Encryption Key" field
- Higher numbers create more scrambled results
- **Remember this key** - you'll need it to decrypt!

### Step 4: Encrypt/Decrypt
- **To Encrypt**: Click "🔒 Encrypt Image"
- **To Decrypt**: Click "🔓 Decrypt Image"
- The result appears in the "Processed Image" panel

### Step 5: Save Result
- Click "💾 Save Result" to save the processed image
- Choose your preferred format and location

## 🔒 Security Notes

⚠️ **Important Security Information**:

- This tool is for **educational purposes** and basic privacy needs
- The encryption method is **simple pixel manipulation** - not cryptographically secure
- For sensitive data, use proper encryption algorithms (AES, RSA, etc.)
- Always keep your encryption key secure and remember it
- Without the correct key, decryption will produce incorrect results

## 🎓 Educational Value

This project teaches:

- **Image Processing Basics**: Understanding pixels and RGB values
- **Encryption Concepts**: Basic encryption/decryption principles
- **GUI Development**: Creating user-friendly interfaces with Tkinter
- **File Handling**: Working with different image formats
- **NumPy Operations**: Array manipulation for image processing

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Report Bugs**: Open an issue if you find any problems
2. **Suggest Features**: Ideas for new functionality
3. **Code Improvements**: Submit pull requests for enhancements
4. **Documentation**: Help improve the documentation

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🔮 Future Enhancements

Potential improvements for future versions:

- [ ] Multiple encryption algorithms (XOR, bit shifting, etc.)
- [ ] Batch processing for multiple images
- [ ] Password-based key generation
- [ ] Image steganography features
- [ ] Advanced encryption methods
- [ ] Command-line interface
- [ ] Progress bars for large images
- [ ] Encryption strength analysis

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you encounter any issues or have questions:

1. Check the existing [Issues](https://github.com/yourusername/image-encryption-tool/issues)
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about the problem
4. Include screenshots if relevant

## 🙏 Acknowledgments

- Built with Python and love ❤️
- Uses Pillow library for image processing
- NumPy for efficient array operations
- Tkinter for the GUI framework

## 📊 Project Stats

- **Language**: Python
- **GUI Framework**: Tkinter
- **Image Processing**: Pillow (PIL)
- **Array Operations**: NumPy
- **Supported Formats**: PNG, JPEG, BMP, TIFF, GIF

---

⭐ If you found this project helpful, please give it a star on GitHub!

**Made with ❤️ for learning and education**

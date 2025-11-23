# 🎄 Last Christmas - Animated Christmas Tree 🎅

A festive Python terminal animation featuring a glowing Christmas tree with synchronized lyrics display!

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Christmas](https://img.shields.io/badge/Spirit-Christmas-red.svg)

## ✨ Features

- 🎄 **Animated Christmas Tree** with colorful glowing lights
- 🎵 **Synchronized Lyrics** displayed in real-time
- 🌈 **Multi-colored Light Effects** that cycle through rainbow colors
- ⭐ **Golden Star** on top of the tree
- 🎨 **Terminal-based Animation** using ANSI colors
## 🎬 Demo

![Christmas Tree Demo](https://github.com/user-attachments/assets/cd0df356-8d84-4966-9927-2420898cb5cc)

The program creates a beautiful animated Christmas tree in your terminal with:
- Lights that glow and change colors continuously
- Lyrics appearing on the right side at equal intervals
- A festive holiday atmosphere right in your command line!
## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- A terminal that supports ANSI color codes

### Clone the Repository
```bash
git clone https://github.com/SanjeevDeori/Last-Christmas.git
cd Last-Christmas
```

## 💻 Usage

Simply run the Python script:

```bash
python christmas_tree.py
```

Or if you're using Python 3 specifically:

```bash
python3 christmas_tree.py
```

### Controls
- Press `Ctrl+C` to stop the animation at any time

## 🎨 Customization

You can easily customize the program by editing these variables in the code:

### Change Lyrics
```python
lyrics = [
    "Your custom lyric line 1",
    "Your custom lyric line 2",
    # Add more lines...
]
```

### Adjust Animation Speed
```python
interval = 1.5  # Change this value to speed up or slow down lyrics
time.sleep(0.2)  # Change this for faster/slower light animation
```

### Modify Colors
```python
COLORS = [
    '\033[91m',  # Red
    '\033[93m',  # Yellow
    '\033[92m',  # Green
    # Add or remove colors as desired
]
```

## 🛠️ How It Works

1. **Tree Structure**: The tree is built using a predefined structure with specific positions for lights
2. **Light Animation**: Lights cycle through colors using ANSI escape codes
3. **Synchronized Display**: Lyrics appear at timed intervals alongside the animated tree
4. **Terminal Clearing**: Screen is refreshed continuously for smooth animation

## 📋 Requirements

- Python 3.6+
- Standard library modules only:
  - `time`
  - `os`

No external dependencies required! 🎉

## 🎄 Tree Structure

```
       *        ← Golden star
      ●●●       
     ●●●●●      
    ●●●●●●●     ← Glowing colored lights
   ●●●●●●●●●    
  ●●●●●●●●●●●   
 ●●●●●●●●●●●●●  
      |||       ← Tree trunk
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new animation patterns
- Improve the light effects
- Add more customization options
- Fix bugs or improve performance

### Steps to Contribute
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - feel free to use it for your holiday celebrations!

## 🎅 Author

**Sanjeev Deori**
- GitHub: [@SanjeevDeori](https://github.com/SanjeevDeori)

## 🌟 Acknowledgments

- Inspired by the festive spirit of Christmas
- Built with ❤️ and Python
- Special thanks to everyone who celebrates the holiday season!

## 📸 Screenshots

![Christmas Tree Demo](https://github.com/user-attachments/assets/cd0df356-8d84-4966-9927-2420898cb5cc)
---

### 🎄 Happy Holidays! 🎅

Made with 💚❤️ for the Christmas season

**Star ⭐ this repository if you enjoyed it!**

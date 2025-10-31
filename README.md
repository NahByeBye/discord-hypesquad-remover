# Discord HypeSquad Badge Remover 🚀

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

A simple and efficient Python script to remove the HypeSquad badge from your Discord account.

## ⚠️ Important Warning

**Using self-bots violates [Discord's Terms of Service](https://discord.com/terms).** This project is provided **for educational purposes only**. Using this script may result in your Discord account being suspended. Use at your own risk.

## ✨ Features

- ✅ Quick HypeSquad badge removal
- 🔒 Secure token management via configuration file
- 📝 Clear and informative error messages
- 🎯 Simple and easy to use

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- A Discord account with a HypeSquad badge

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/NahByeBye/discord-hypesquad-remover.git
cd discord-hypesquad-remover
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure your token:**
```bash
# Copy the example file
cp config.example.json config.json

# Edit config.json and add your token
```

## 🔧 Configuration

1. Create a copy of `config.example.json` named `config.json`
2. Open `config.json` and replace `YOUR_TOKEN_HERE` with your Discord token

### How to get your Discord token?

> ⚠️ **WARNING:** NEVER share your token with anyone! Your token gives full access to your account.

**Method 1 - Browser Console (Recommended):**

1. Open Discord in your web browser (discord.com)
2. Press `F12` to open developer tools
3. Go to the `Console` tab
4. Paste this command and press Enter:
```javascript
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```
5. Copy the token that appears (without quotes)
6. Paste it into your `config.json` file

**Method 2 - Discord Application:**

1. Open Discord
2. Press `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac)
3. Follow the same steps as Method 1

## 💻 Usage

Simply run the script:
```bash
python remove_hypesquad.py
```

The script will display:
- ✅ A success message if the badge is removed
- ⚠️ A warning if you don't have a HypeSquad badge
- ❌ An error if the token is invalid

## 📸 Preview

```
==================================================
  Self-Bot - Discord HypeSquad Badge Removal
==================================================

🔄 Attempting to remove HypeSquad badge...
✅ HypeSquad badge successfully removed!

==================================================
```

## 🛠️ Troubleshooting

### "Invalid or expired token"
- Make sure you copied the complete token
- Generate a new token by changing your Discord password

### "You don't have a HypeSquad badge"
- Check that you have an active HypeSquad badge
- Check your Discord settings > HypeSquad

### Import errors
```bash
pip install --upgrade -r requirements.txt
```

## 🔒 Security

- ⚠️ NEVER commit your `config.json` with your real token
- 🔐 The `config.json` file is in `.gitignore` by default
- 🚨 If your token is compromised, change your Discord password **immediately**
- 📝 Use `config.example.json` as a template

## 📝 Notes

- The script only removes the HypeSquad Online badge
- You can add it back anytime from Discord settings
- No data is collected or sent anywhere other than the official Discord API

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ⚖️ Disclaimer

This project is provided "as is", without warranty of any kind. The authors are not responsible for any Discord account suspension or ban resulting from the use of this script. Use it knowingly and at your own risk.

---

**Created by d_1114**

**Developed with ❤️ for the Discord community**

⭐ If this project was useful to you, feel free to give it a star!

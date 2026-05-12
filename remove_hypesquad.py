"""
Discord HypeSquad Badge Remover
Author: d_1114
GitHub: https://github.com/NahByeBye/discord-hypesquad-remover
"""

import requests
import json
import os
import sys

def create_config_file():
    """Create config.json file with template and exit"""
    config_template = {
        "token": "input_your_token_here"
    }
    
    with open('config.json', 'w') as f:
        json.dump(config_template, f, indent=4)
    
    print("config.json file not found!")
    print("Created config.json file with template.")
    print("Please edit config.json and add your token, then run the program again.")
    print("\nPress Enter to exit...")
    input()
    sys.exit(0)

def load_config():
    """Load token from config.json file"""
    if not os.path.exists('config.json'):
        create_config_file()
    
    with open('config.json', 'r') as f:
        config = json.load(f)
        return config.get('token')

def remove_hypesquad(token):
    """Remove HypeSquad badge from Discord account"""
    url = "https://discord.com/api/v9/hypesquad/online"
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    print("🔄 Attempting to remove HypeSquad badge...")
    
    try:
        response = requests.delete(url, headers=headers)
        
        if response.status_code == 204:
            print("✅ HypeSquad badge successfully removed!")
            return True
        elif response.status_code == 401:
            print("❌ Invalid or expired token!")
            return False
        elif response.status_code == 404:
            print("⚠️  You don't have a HypeSquad badge to remove.")
            return False
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Request error: {str(e)}")
        return False

def main():
    print("=" * 50)
    print("  Self-Bot - Discord HypeSquad Badge Removal")
    print("=" * 50)
    print()
    
    token = load_config()
    
    if not token:
        print("❌ No token found in config.json!")
        print("Please edit config.json and add your token.")
        print("\nPress Enter to exit...")
        input()
        return

    if token == "input_your_token_here":
        print("❌ Please edit config.json and replace 'input_your_token_here' with your actual token!")
        print("\nPress Enter to exit...")
        input()
        return

    if not token.strip():
        print("❌ Token is empty in config.json!")
        return
    
    remove_hypesquad(token)
    
    print()
    print("=" * 50)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

"""
Discord HypeSquad Badge Remover
Author: d_1114
GitHub: https://github.com/NahByeBye/discord-hypesquad-remover
"""

import requests
import json
import os

def load_config():
    """Load token from config.json file"""
    if not os.path.exists('config.json'):
        print("❌ config.json file not found!")
        print("Create a config.json file with the following content:")
        print('{\n  "token": "YOUR_TOKEN_HERE"\n}')
        return None
    
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
        return
    
    # Token validation
    if not token.strip():
        print("❌ Token is empty in config.json!")
        return
    
    remove_hypesquad(token)
    
    print()
    print("=" * 50)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

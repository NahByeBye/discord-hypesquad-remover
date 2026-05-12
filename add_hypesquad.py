"""
Discord HypeSquad Badge Adder
Author: d_1114
GitHub: https://github.com/NahByeBye/discord-hypesquad-remover
"""

import requests
import json
import os

def load_config():
    """Load token from config.json file"""
    if not os.path.exists('config.json'):
        print("config.json file not found!")
        print("Create a config.json file with the following content:")
        print('{\n  "token": "YOUR_TOKEN_HERE"\n}')
        return None
    
    with open('config.json', 'r') as f:
        config = json.load(f)
        return config.get('token')

def add_hypesquad(token, house):
    """Add HypeSquad badge to Discord account"""
    url = "https://discord.com/api/v9/hypesquad/online"
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    data = {
        "house_id": house
    }
    
    print(f"Attempting to join HypeSquad house {house}...")
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 204:
            houses = {1: "Bravery", 2: "Brilliance", 3: "Balance"}
            print(f"Successfully joined HypeSquad {houses.get(house, 'Unknown')}!")
            return True
        elif response.status_code == 401:
            print("❌ Invalid or expired token!")
            return False
        elif response.status_code == 400:
            print("Bad request. You might already have a HypeSquad badge.")
            return False
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"Request error: {str(e)}")
        return False

def main():
    print("=" * 50)
    print("  Self-Bot - Discord HypeSquad Badge Adder")
    print("=" * 50)
    print()
    
    token = load_config()
    
    if not token:
        return
    
    # Token validation
    if not token.strip():
        print("❌ Token is empty in config.json!")
        return
    
    print("Choose your HypeSquad house:")
    print("1. Bravery (Purple)")
    print("2. Brilliance (Orange)")
    print("3. Balance (Green)")
    print()
    
    try:
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice not in ['1', '2', '3']:
            print("Invalid choice! Please select 1, 2, or 3.")
            return
        
        house_id = int(choice)
        add_hypesquad(token, house_id)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    print()
    print("=" * 50)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

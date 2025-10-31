import requests
import json
import os

def load_config():
    """Charge le token depuis le fichier config.json"""
    if not os.path.exists('config.json'):
        print("❌ Fichier config.json introuvable!")
        print("Créez un fichier config.json avec le contenu suivant:")
        print('{\n  "token": "VOTRE_TOKEN_ICI"\n}')
        return None
    
    with open('config.json', 'r') as f:
        config = json.load(f)
        return config.get('token')

def remove_hypesquad(token):
    """Retire le badge HypeSquad du compte Discord"""
    url = "https://discord.com/api/v9/hypesquad/online"
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    print("🔄 Tentative de retrait du badge HypeSquad...")
    
    try:
        response = requests.delete(url, headers=headers)
        
        if response.status_code == 204:
            print("✅ Badge HypeSquad retiré avec succès!")
            return True
        elif response.status_code == 401:
            print("❌ Token invalide ou expiré!")
            return False
        elif response.status_code == 404:
            print("⚠️  Vous n'avez pas de badge HypeSquad à retirer.")
            return False
        else:
            print(f"❌ Erreur: {response.status_code}")
            print(f"Réponse: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors de la requête: {str(e)}")
        return False

def main():
    print("=" * 50)
    print("  Self-Bot - Retrait Badge HypeSquad Discord")
    print("=" * 50)
    print()
    
    token = load_config()
    
    if not token:
        return
    
    # Vérification du token
    if not token.strip():
        print("❌ Le token est vide dans config.json!")
        return
    
    remove_hypesquad(token)
    
    print()
    print("=" * 50)
    input("Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()

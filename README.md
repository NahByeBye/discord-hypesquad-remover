# Discord HypeSquad Badge Remover 🚀

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

Un script Python simple et efficace pour retirer le badge HypeSquad de votre compte Discord.

## ⚠️ Avertissement Important

**L'utilisation de self-bots viole les [Conditions d'Utilisation de Discord](https://discord.com/terms).** Ce projet est fourni **à des fins éducatives uniquement**. L'utilisation de ce script peut entraîner la suspension de votre compte Discord. Utilisez à vos propres risques.

## ✨ Fonctionnalités

- ✅ Retrait rapide du badge HypeSquad
- � Gestion sécurisée du token via fichier de configuration
- 📝 Messages d'erreur clairs et informatifs
- 🎯 Simple et facile à utiliser

## 📋 Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)
- Un compte Discord avec un badge HypeSquad

## 🚀 Installation

1. **Clonez le dépôt :**
```bash
git clone https://github.com/VOTRE_USERNAME/discord-hypesquad-remover.git
cd discord-hypesquad-remover
```

2. **Installez les dépendances :**
```bash
pip install -r requirements.txt
```

3. **Configurez votre token :**
```bash
# Copiez le fichier exemple
cp config.example.json config.json

# Éditez config.json et ajoutez votre token
```

## 🔧 Configuration

1. Créez une copie de `config.example.json` nommée `config.json`
2. Ouvrez `config.json` et remplacez `VOTRE_TOKEN_ICI` par votre token Discord

### Comment obtenir votre token Discord ?

> ⚠️ **ATTENTION:** Ne partagez JAMAIS votre token avec qui que ce soit ! Votre token donne un accès complet à votre compte.

**Méthode 1 - Console du Navigateur (Recommandée) :**

1. Ouvrez Discord dans votre navigateur web (discord.com)
2. Appuyez sur `F12` pour ouvrir les outils de développement
3. Allez dans l'onglet `Console`
4. Collez cette commande et appuyez sur Entrée :
```javascript
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```
5. Copiez le token qui s'affiche (sans les guillemets)
6. Collez-le dans votre fichier `config.json`

**Méthode 2 - Application Discord :**

1. Ouvrez Discord
2. Appuyez sur `Ctrl + Shift + I` (Windows/Linux) ou `Cmd + Option + I` (Mac)
3. Suivez les mêmes étapes que la méthode 1

## � Utilisation

Exécutez simplement le script :
```bash
python remove_hypesquad.py
```

Le script affichera :
- ✅ Un message de succès si le badge est retiré
- ⚠️ Un avertissement si vous n'avez pas de badge HypeSquad
- ❌ Une erreur si le token est invalide

## 📸 Aperçu

```
==================================================
  Self-Bot - Retrait Badge HypeSquad Discord
==================================================

🔄 Tentative de retrait du badge HypeSquad...
✅ Badge HypeSquad retiré avec succès!

==================================================
```

## 🛠️ Dépannage

### "Token invalide ou expiré"
- Vérifiez que vous avez copié le token complet
- Régénérez un nouveau token en changeant votre mot de passe Discord

### "Vous n'avez pas de badge HypeSquad"
- Vérifiez que vous avez bien un badge HypeSquad actif
- Consultez vos paramètres Discord > HypeSquad

### Erreurs d'importation
```bash
pip install --upgrade -r requirements.txt
```

## 🔒 Sécurité

- ⚠️ Ne commitez **JAMAIS** votre `config.json` avec votre vrai token
- 🔐 Le fichier `config.json` est dans `.gitignore` par défaut
- 🚨 Si votre token est compromis, changez **immédiatement** votre mot de passe Discord
- 📝 Utilisez `config.example.json` comme template

## 📝 Notes

- Le script retire uniquement le badge HypeSquad Online
- Vous pourrez le remettre à tout moment depuis les paramètres Discord
- Aucune donnée n'est collectée ou envoyée ailleurs que vers l'API Discord officielle

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- 🐛 Signaler des bugs
- 💡 Proposer de nouvelles fonctionnalités
- 🔧 Soumettre des pull requests

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## ⚖️ Disclaimer

Ce projet est fourni "tel quel", sans garantie d'aucune sorte. Les auteurs ne sont pas responsables de toute suspension ou bannissement de compte Discord résultant de l'utilisation de ce script. Utilisez-le en connaissance de cause et à vos propres risques.

---

**Développé avec ❤️ pour la communauté Discord**

⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile !


# 📝 Cover Letter Writer Agent

Petit projet se voulant simple, accessible et pratique, permettant à l'aide d'un agent + LLM d'avoir une base pour une lettre de motivation à une offre d'emploi dont on aura donné la description, ainsi que celle du candidat - plus ou moins brièvement, selon le niveau de détail attendu.

*Pattern utilisé : thinking/reasoning/reflection*

## 💻 Environnement

- [VSCodium 1.99.32846](https://github.com/VSCodium/vscodium/releases)
- Anaconda3 2024.10-1
- [Python 3.12.7](https://www.python.org/downloads/)

## 🚀 Utilisation

Pour installer les dépendances, on utilise [uv](https://docs.astral.sh/uv/) :
> pip install uv

Pour lancer le script :
> uv run main.py

❗ **Il faudra au préalable veiller à fournir une clé API [Groq](https://groq.com/) dans un fichier** `.env` :
> GROQ_API_KEY = "your-API-key"

Pour installer les dépendances manuellement :
> uv add agno groq python-dotenv

## 📸 Exemple d'utilisation

![lm-n2_n1](https://github.com/user-attachments/assets/b2dcc1e4-54f7-43c0-98ac-a48bf015d4d0)

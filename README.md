Markdown
# 🎙️ Voice Support DPE - Assistant Vocal de Diagnostic Énergétique

Un assistant vocal interactif en **Voice AI / MLOps** capable de comprendre les caractéristiques d'un logement dictées à l'oral, d'extraire les entités clés (surface, année de construction, type de bien) et de fournir une estimation instantanée de la consommation énergétique (DPE) sous forme de synthèse vocale fluide en français.

---

## 🚀 Fonctionnalités Clés

* **🎙️ Speech-to-Text (STT) & Traitement NLP :** Capture la voix ou le texte utilisateur et extrait automatiquement les variables stratégiques du logement (surface en $m^2$, année de construction, type de logement).
* **🧠 Moteur Inférence DPE (ML) :** Interfère avec un algorithme de Machine Learning (XGBoost) pour estimer la consommation énergétique ($kWh/m^2/an$) et la classe DPE (de $A$ à $G$).
* **🔊 Text-to-Speech (TTS) Haute Qualité :** Synthétise et restitue une réponse vocale naturelle et réaliste en français grâce au moteur neural `edge-tts`.
* **⚙️ Architecture Extensible :** Conçu pour s'intégrer facilement avec une API REST (`FastAPI`) et des pipelines de déploiement conteneurisés (`Docker`).

---

## 🛠️ Stack Technique

* **Langage :** Python 3.10+
* **Speech-to-Text (STT) :** `SpeechRecognition`
* **Text-to-Speech (TTS) :** `edge-tts` (Microsoft Neural Voices)
* **Traitement de Données & NLP :** Regex, Scikit-Learn, SciPy
* **Versioning & CI/CD :** Git, GitHub

---

## 📁 Structure du Projet

```text
voice-dpe-assistant/
├── voice_assistant.py     # Pipeline principal (NLP + Inférence ML + TTS)
├── test_tts.py            # Script de test unitaire pour la synthèse vocale
├── test_stt.py            # Script de test pour la reconnaissance vocale
├── requirements.txt       # Dépendances Python du projet
├── .gitignore             # Fichiers ignorés par Git
└── README.md              # Documentation du projet
💻 Installation & Utilisation
1. Cloner le dépôt & installer les dépendances
Bash
git clone [https://github.com/cheikhtidianediouf/voice-dpe-assistant.git](https://github.com/cheikhtidianediouf/voice-dpe-assistant.git)
cd voice-dpe-assistant

# Créer un environnement virtuel (optionnel mais recommandé)
python -m venv envVoice
# Sur Windows
envVoice\Scripts\activate

# Installer les dépendances
python -m pip install -r requirements.txt
2. Lancer l'assistant vocal
Bash
python voice_assistant.py
📊 Exemple d'Exécution
Entrée (Utilisateur) :

"J'ai un appartement de 85 mètres carrés construit en 2015"

Traitement IA & MLOps :

Données extraites : Surface = 85.0 m² | Année = 2015 | Type = Appartement

Inférence ML : Consommation estimée = 137.5 kWh/m²/an | Classe DPE = C

Sortie (Audio) :

🔊 "D'après mes calculs pour votre Appartement de 85 mètres carrés, la consommation énergétique estimée est de 137.5 kilowattheures par mètre carré par an. Votre logement est classé en étiquette énergétique C."
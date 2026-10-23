import asyncio
import edge_tts

# Texte de réponse de notre assistant DPE
TEXTE = "Bonjour ! Je suis votre assistant vocal DPE. Votre consommation énergétique estimée est de 152 kilowattheures par mètre carré par an."

# Voix française naturelle d'Microsoft Edge (Henri ou Denise)
VOICE = "fr-FR-HenriNeural" 
OUTPUT_FILE = "reponse_assistant.mp3"

async def main():
    communicate = edge_tts.Communicate(TEXTE, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"✅ Fichier audio généré avec succès : {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
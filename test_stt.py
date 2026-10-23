import speech_recognition as sr

def transcrire_audio(fichier_audio):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(fichier_audio) as source:
        print("🔊 Lecture et analyse du fichier audio...")
        audio = recognizer.record(source)
        
    try:
        texte = recognizer.recognize_google(audio, language="fr-FR")
        print(f"✅ Texte transcrit : '{texte}'")
        return texte
    except sr.UnknownValueError:
        print("❌ L'assistant n'a pas compris l'audio.")
        return None
    except sr.RequestError as e:
        print(f"❌ Erreur du service de reconnaissance : {e}")
        return None

if __name__ == "__main__":
    # Testez avec un fichier audio .wav si vous en avez un, ou préparez la fonction
    print("Module STT prêt pour l'intégration !")
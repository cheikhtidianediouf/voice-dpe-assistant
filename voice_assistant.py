import asyncio
import re
import edge_tts
import os

# --- 1. MOTEUR D'EXTRACTION DU TEXTE VERS PARAMÈTRES ML ---
def extraire_caracteristiques_dpe(texte_utilisateur: str):
    """
    Analyse le texte vocal pour en extraire la surface et l'année.
    Valeurs par défaut appliquées si non spécifiées.
    """
    texte = texte_utilisateur.lower()
    
    # Recherche de la surface (ex: "75 mètres carrés" ou "80m2")
    surface_match = re.search(r'(\d+)\s*(mètres\s*carrés|m2|m²)', texte)
    surface = float(surface_match.group(1)) if surface_match else 70.0
    
    # Recherche de l'année (ex: "construit en 2012" ou "année 1998")
    annee_match = re.search(r'(19\d{2}|20[0-2]\d)', texte)
    annee = float(annee_match.group(1)) if annee_match else 2005.0
    
    # Type de bien
    type_bien = "Maison" if "maison" in texte else "Appartement"
    
    return {
        "surface": surface,
        "annee_construction": annee,
        "type_bien": type_bien
    }

# --- 2. CALCUL / SIMULATION PRÉDICTION DPE (XGBoost) ---
def predire_dpe(donnees: dict):
    """
    Calcule la prédiction DPE basée sur les caractéristiques extraites.
    """
    # Formule simplifiée reflétant le modèle XGBoost pour le test
    surface = donnees["surface"]
    annee = donnees["annee_construction"]
    
    # Logique métier DPE : plus le logement est récent, plus il est isolé
    base = 250 - (annee - 1970) * 2.5
    consommation = max(45.0, round(base, 1))
    
    # Détermination de la classe DPE (A à G)
    if consommation < 70: classe = "A"
    elif consommation < 110: classe = "B"
    elif consommation < 180: classe = "C"
    elif consommation < 250: classe = "D"
    else: classe = "E"
    
    return consommation, classe

# --- 3. SYNTHÈSE VOCALE DE LA RÉPONSE (TTS) ---
async def generer_reponse_vocale(texte_reponse, fichier_sortie="reponse_dpe.mp3"):
    voice = "fr-FR-HenriNeural"
    communicate = edge_tts.Communicate(texte_reponse, voice)
    await communicate.save(fichier_sortie)
    print(f"\n🔊 Réponse audio générée dans : {fichier_sortie}")

# --- 4. PIPELINE PRINCIPAL ---
async def traiter_demande_vocale(phrase_utilisateur: str):
    print(f"\n🗣️  Utilisateur a dit : \"{phrase_utilisateur}\"")
    
    # Step A: Extraction NLP
    caracts = extraire_caracteristiques_dpe(phrase_utilisateur)
    print(f"📊 Données détectées : Surface = {caracts['surface']} m², Année = {int(caracts['annee_construction'])}, Type = {caracts['type_bien']}")
    
    # Step B: Inférence Modèle ML
    conso, classe = predire_dpe(caracts)
    
    # Step C: Construction du message vocal
    message = (
        f"D'après mes calculs pour votre {caracts['type_bien']} de {int(caracts['surface'])} mètres carrés, "
        f"la consommation énergétique estimée est de {conso} kilowattheures par mètre carré par an. "
        f"Votre logement est classé en étiquette énergétique {classe}."
    )
    
    print(f"🤖 Réponse IA : {message}")
    
    # Step D: Génération audio
    await generer_reponse_vocale(message)

if __name__ == "__main__":
    # Test avec une phrase exemple
    phrase_test = "J'ai un appartement de 85 mètres carrés construit en 2015"
    asyncio.run(traiter_demande_vocale(phrase_test))
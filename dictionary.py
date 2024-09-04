# Create two dictionaries: English to Spanish and Spanish to German
etos = {
    "hello": "hola",
    "goodbye": "adiós",
    "friend": "amigo",
    "house": "casa",
    "car": "coche"
}

stog = {
    "hola": "Hallo",
    "adiós": "Auf Wiedersehen",
    "amigo": "Freund",
    "casa": "Haus",
    "coche": "Auto"
}

eword = input("Enter a word in English: ")

if eword in etos:
    sword = etos[eword]
    
    if sword in stog:
        gword = stog[sword]
        print(f"The German translation of '{eword}' is '{gword}'.")
    else:
        print(f"Sorry, I don't know the German translation of '{sword}'.")
else:
    print(f"Sorry, I don't know the Spanish translation of '{eword}'.")
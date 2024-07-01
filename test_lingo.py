from lingo import Lingo
if __name__ == "__main__":
    # Maak een instantie van de Lingo klasse
    lingo_spel = Lingo()

    # Test verschillende inputs en print de resultaten
    test_woorden = ["apple", "apels", "alepp", "lapel", "mango"]
    
    for test_woord in test_woorden:
        resultaat = lingo_spel.validate_input(test_woord)
        print(f"Invoer: {test_woord} - Resultaat: {resultaat}")

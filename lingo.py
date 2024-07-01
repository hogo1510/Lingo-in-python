class Lingo:
    def __init__(self):
        # Hier kun je later de waarde van 'woord' variabel maken
        self.woord = "appel"  # Stel een woord van vijf letters in

    def validate_input(self, input_woord):
        if len(input_woord) != 5:
            return "Input moet precies 5 letters zijn."
        
        resultaat = ["_"] * 5
        for i in range(5):
            if input_woord[i] == self.woord[i]:
                resultaat[i] = input_woord[i]
            elif input_woord[i] in self.woord:
                resultaat[i] = "*"

        return "".join(resultaat)

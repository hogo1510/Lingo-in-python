import tkinter as tk

from lingo import Lingo

class LingoGUI:
    def __init__(self, root):
        self.lingo_spel = Lingo()
        
        # Titel Label
        self.title_label = tk.Label(root, text="Lingo Spel", font=("Helvetica", 24))
        self.title_label.pack(pady=10)
        
        # Welkomsttekst
        self.welcome_text = tk.Label(root, text="Welkom bij het Lingo spel! Raad het vijf-letter woord.", font=("Helvetica", 14))
        self.welcome_text.pack(pady=10)
        
        # Invoer veld
        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.validate)
        
        # Resultaat Label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)
        
        # Status Label
        self.status_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.status_label.pack(pady=10)
        
    def validate(self, event):
        user_input = self.entry.get()
        resultaat = self.lingo_spel.validate_input(user_input)
        self.result_label.config(text=f"Resultaat: {resultaat}")
        
        if resultaat == self.lingo_spel.woord:
            self.status_label.config(text="Gefeliciteerd, je hebt gewonnen!")
        else:
            self.status_label.config(text="Probeer opnieuw!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LingoGUI(root)
    root.title("Lingo Spel")
    root.mainloop()

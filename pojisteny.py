class Pojisteny:

    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def __str__(self):
        return f"Jméno: {self.jmeno} " \
               f"\nPřijmení: {self.prijmeni} " \
               f"\nVěk: {self.vek} " \
               f"\nTelefonní číslo: {self.tel_cislo}"
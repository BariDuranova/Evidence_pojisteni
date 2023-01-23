from pojisteny import Pojisteny

class Evidence:
    print("Vítejte v evidenci pojištění.\n")

    def __init__(self):
        self.pojistenci = []

    def vypsat_uvod(self):
        print("1. Přidat pojištěného")
        print("2. Vyhledat pojištěného")
        print("3. Zobrazit seznam všech pojištěných")
        print("4. Ukončit aplikaci\n")

    def zalozit(self):
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = int(input("Zadejte věk: "))
        tel_cislo = int(input("Zadejte telefonní číslo: "))
        pojistenec = Pojisteny(jmeno, prijmeni, vek, tel_cislo)
        self.pojistenci.append(pojistenec)
        print("\nPojištěnec byl úspěšně přidán.\n")

    def vyhledat(self):
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        for pojisteny in self.pojistenci:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print(pojisteny,"\n")
                break
        else:
            print("Takové údaje o pojištěném v naší databázi nemáme.\n")

    def vypsat_seznam(self):
        for pojistenec in self.pojistenci:
            print(pojistenec,"\n")

    def spustit(self):

        while True:
            self.vypsat_uvod()
            volba = input("Zvolte volbu v programu pro evidenci pojištěnců.\n")

            if volba == "1":
                self.zalozit()
            elif volba == "2":
                self.vyhledat()
            elif volba == "3":
                self.vypsat_seznam()
            elif volba == "4":
                print("Program na evidenci pojištěnců je ukončen.")
                break
            else:
                print("Neplatná volba.\n")
